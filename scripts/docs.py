import json
import logging
import os
import re
import shutil
import subprocess
from functools import lru_cache
from http.server import HTTPServer, SimpleHTTPRequestHandler
from importlib import metadata
from multiprocessing import Pool
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import cligenius
import mkdocs.utils
import yaml
from jinja2 import Template
from ruff.__main__ import find_ruff_bin

logging.basicConfig(level=logging.INFO)

app = cligenius.Cligenius()

mkdocs_name = "mkdocs.yml"
missing_translation_snippet = "{!../../docs/missing-translation.md!}"
non_translated_sections = [
    "reference/",
    "release-notes.md",
    "readyapi-people.md",
    "external-links.md",
    "newsletter.md",
    "management-tasks.md",
    "management.md",
    "contributing.md",
]

docs_path = Path("docs")
en_docs_path = Path("docs/en")
en_config_path = en_docs_path / mkdocs_name
site_path = Path("site").absolute()
build_site_path = Path("site_build").absolute()

index_sponsors_template = """
{% if sponsors %}
{% for sponsor in sponsors.gold -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}"></a>
{% endfor -%}
{%- for sponsor in sponsors.silver -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}"></a>
{% endfor %}
{% endif %}
"""


@lru_cache
def is_mkdocs_insiders() -> bool:
    version = metadata.version("mkdocs-material")
    return "insiders" in version


def get_en_config() -> Dict[str, Any]:
    return mkdocs.utils.yaml_load(en_config_path.read_text(encoding="utf-8"))


def get_lang_paths() -> List[Path]:
    return sorted(docs_path.iterdir())


def lang_callback(lang: Optional[str]) -> Union[str, None]:
    return lang.lower() if lang else None


def complete_existing_lang(incomplete: str):
    for lang_path in get_lang_paths():
        if lang_path.is_dir() and lang_path.name.startswith(incomplete):
            yield lang_path.name


@app.callback()
def callback() -> None:
    if is_mkdocs_insiders():
        os.environ["INSIDERS_FILE"] = "../en/mkdocs.insiders.yml"
    os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/homebrew/lib"


@app.command()
def new_lang(lang: str = cligenius.Argument(..., callback=lang_callback)):
    new_path = Path("docs") / lang
    if new_path.exists():
        cligenius.echo(f"The language was already created: {lang}")
        raise cligenius.Abort()
    new_path.mkdir()
    (new_path / mkdocs_name).write_text("INHERIT: ../en/mkdocs.yml\n", encoding="utf-8")
    (new_path / "docs").mkdir()
    en_index = en_docs_path / "docs" / "index.md"
    new_index = new_path / "docs" / "index.md"
    content = f"{missing_translation_snippet}\n\n{en_index.read_text('utf-8')}"
    new_index.write_text(content, encoding="utf-8")
    cligenius.secho(
        f"Successfully initialized: {new_path}", color=cligenius.colors.GREEN
    )
    update_languages()


@app.command()
def build_lang(
    lang: str = cligenius.Argument(
        ..., callback=lang_callback, autocompletion=complete_existing_lang
    ),
):
    cligenius.echo(f"Building docs for: {lang}")
    lang_path = Path("docs") / lang
    if not lang_path.is_dir():
        cligenius.echo(f"The language translation doesn't exist: {lang}")
        raise cligenius.Abort()

    dist_path = site_path if lang == "en" else site_path / lang
    build_site_dist_path = build_site_path / lang

    if lang != "en":
        shutil.rmtree(dist_path, ignore_errors=True)
    shutil.rmtree(build_site_dist_path, ignore_errors=True)

    os.chdir(lang_path)
    subprocess.run(
        ["mkdocs", "build", "--site-dir", str(build_site_dist_path)], check=True
    )
    shutil.copytree(build_site_dist_path, dist_path, dirs_exist_ok=True)
    os.chdir("..")
    cligenius.secho(
        f"Successfully built docs for: {lang}", color=cligenius.colors.GREEN
    )


def generate_readme_content() -> str:
    en_index = en_docs_path / "docs" / "index.md"
    content = en_index.read_text("utf-8")
    match_pre = re.search(r"</style>\n\n", content)
    match_start = re.search(r"<!-- sponsors -->", content)
    match_end = re.search(r"<!-- /sponsors -->", content)
    if not (match_start and match_end and match_pre):
        raise RuntimeError("Failed to parse sponsors section in index.md")
    sponsors_data = mkdocs.utils.yaml_load(
        (en_docs_path / "data/sponsors.yml").read_text("utf-8")
    )
    message = Template(index_sponsors_template).render(sponsors=sponsors_data)

    new_content = (
        content[match_pre.end() : match_start.end()]
        + message
        + content[match_end.start() :]
    )
    return re.sub(
        r"<!-- only-mkdocs -->.*?<!-- /only-mkdocs -->",
        "",
        new_content,
        flags=re.DOTALL,
    )


def _get_readme_path() -> Path:
    return Path("README.md")


def _readme_needs_update() -> bool:
    return _get_readme_path().read_text("utf-8") != generate_readme_content()


def _update_readme() -> None:
    _get_readme_path().write_text(generate_readme_content(), encoding="utf-8")


@app.command()
def verify_readme(auto_fix: bool = False) -> None:
    cligenius.echo("Verifying README.md...")
    if _readme_needs_update():
        cligenius.secho(
            "README.md is outdated from index.md", color=cligenius.colors.RED
        )
        if auto_fix:
            _update_readme()
            cligenius.secho("README.md auto-fixed ✅", color=cligenius.colors.GREEN)
        else:
            raise cligenius.Abort()
    else:
        cligenius.echo("Valid README ✅")


@app.command()
def fix_readme() -> None:
    cligenius.echo("Fixing README.md...")
    _update_readme()
    cligenius.secho("README.md updated ✅", color=cligenius.colors.GREEN)


@app.command()
def build_all() -> None:
    update_languages()
    shutil.rmtree(site_path, ignore_errors=True)
    langs = [lang.name for lang in get_lang_paths() if lang.is_dir()]
    with Pool((os.cpu_count() or 1) * 4) as p:
        p.map(build_lang, langs)


@app.command()
def update_languages() -> None:
    update_config()


@app.command()
def serve() -> None:
    os.chdir("site")
    server = HTTPServer(("", 8008), SimpleHTTPRequestHandler)
    cligenius.echo("Serving at http://127.0.0.1:8008")
    server.serve_forever()


@app.command()
def live(
    lang: str = cligenius.Argument(
        None, callback=lang_callback, autocompletion=complete_existing_lang
    ),
    dirty: bool = False,
) -> None:
    if lang is None:
        lang = "en"
    args = ["mkdocs", "serve", "--dev-addr", "127.0.0.1:8008"]
    if dirty:
        args.append("--dirty")
    subprocess.run(
        args, env={**os.environ, "LINENUMS": "true"}, cwd=docs_path / lang, check=True
    )


def get_updated_config_content() -> Dict[str, Any]:
    config = get_en_config()
    languages = [{"en": "/"}]
    local_names_path = Path(__file__).parent / "../docs/language_names.yml"
    local_names = mkdocs.utils.yaml_load(local_names_path.read_text("utf-8"))
    for lang_path in get_lang_paths():
        code = lang_path.name
        if code in {"en", "em"} or not lang_path.is_dir():
            continue
        if code not in local_names:
            print(f"Missing language name for: {code}")
            raise cligenius.Abort()
        languages.append({code: f"/{code}/"})
    config["extra"]["alternate"] = [
        {"link": url, "name": f"{code} - {local_names[code]}"}
        for lang in languages
        for code, url in lang.items()
    ] + [{"link": "/em/", "name": "😉"}]
    return config


def update_config() -> None:
    config = get_updated_config_content()
    en_config_path.write_text(
        yaml.dump(config, sort_keys=False, width=200, allow_unicode=True),
        encoding="utf-8",
    )


@app.command()
def verify_config() -> None:
    cligenius.echo("Verifying mkdocs.yml")
    if get_en_config() != get_updated_config_content():
        cligenius.secho("docs/en/mkdocs.yml is outdated", color=cligenius.colors.RED)
        raise cligenius.Abort()
    cligenius.echo("Valid mkdocs.yml ✅")


@app.command()
def verify_non_translated() -> None:
    cligenius.echo("Verifying non-translated pages...")
    error_paths = []
    for lang in get_lang_paths():
        if lang.name == "en":
            continue
        for nt in non_translated_sections:
            path = lang / "docs" / nt
            if path.exists():
                error_paths.append(path)
    if error_paths:
        for path in error_paths:
            print(path)
        raise cligenius.Abort()
    cligenius.echo("No non-translated pages found ✅")


@app.command()
def verify_docs():
    verify_readme()
    verify_config()
    verify_non_translated()


@app.command()
def langs_json():
    langs = [lang.name for lang in get_lang_paths() if lang.is_dir()]
    print(json.dumps(langs))


@app.command()
def generate_docs_src_versions_for_file(file_path: Path) -> None:
    targets = ["py39", "py310"]
    base_content = file_path.read_text("utf-8")
    seen = {base_content}
    for version in targets:
        result = subprocess.run(
            [
                find_ruff_bin(),
                "check",
                "--target-version",
                version,
                "--fix",
                "--unsafe-fixes",
                "-",
            ],
            input=base_content.encode("utf-8"),
            capture_output=True,
        )
        formatted = subprocess.run(
            [find_ruff_bin(), "format", "-"], input=result.stdout, capture_output=True
        ).stdout.decode("utf-8")
        if formatted not in seen:
            seen.add(formatted)
            versioned_file = file_path.with_name(
                file_path.name.replace(".py", f"_{version}.py")
            )
            versioned_file.write_text(formatted, encoding="utf-8")


if __name__ == "__main__":
    app()
