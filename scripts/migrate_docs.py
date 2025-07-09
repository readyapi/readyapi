#!/usr/bin/env python3
"""
Documentation Migration Script for ReadyAPI

This script helps migrate documentation to the new structure.
"""

import os
import re
import shutil
from pathlib import Path
from typing import Dict, List

import yaml

# Configuration
BASE_DIR = Path(__file__).parent.parent
DOCS_DIR = BASE_DIR / "docs"
SRC_DIR = DOCS_DIR / "en" / "docs"
DEST_DIR = DOCS_DIR / "en" / "docs" / "new_structure"

# Define the new structure
NEW_STRUCTURE = {
    "getting-started": ["installation.md", "quickstart.md", "tutorial/", "features.md"],
    "guides": [
        "async.md",
        "python-types.md",
        "environment-variables.md",
        "virtual-environments.md",
    ],
    "advanced": ["middleware.md", "dependencies/", "security/", "graphql/", "grpc/"],
    "deployment": ["docker.md", "kubernetes.md", "aws.md", "gcp.md", "azure.md"],
    "reference": ["api/", "models/", "exceptions/"],
    "community": ["contributing.md", "code-of-conduct.md", "help-readyapi.md"],
}


def ensure_directory(path: Path) -> None:
    """Ensure directory exists."""
    path.mkdir(parents=True, exist_ok=True)


def copy_file(src: Path, dest: Path) -> None:
    """Copy file with logging."""
    print(f"Copying {src} to {dest}")
    shutil.copy2(src, dest)


def update_links(content: str, path_mapping: Dict[str, str]) -> str:
    """Update markdown links in content based on path mapping."""
    for old_path, new_path in path_mapping.items():
        # Handle relative links
        content = re.sub(
            rf"\]\(([.\/]*?){re.escape(old_path)}(#[^)]*)?\)",
            f"]({new_path}\2)",
            content,
        )
        # Handle reference links
        content = re.sub(
            rf'\[([^\]]+)\]:\s*([.\/]*?){re.escape(old_path)}(#[^\s]*)?(\s|"|$)',
            f"[\1]: {new_path}\3\4",
            content,
        )
    return content


def migrate_files() -> None:
    """Migrate files to new structure."""
    path_mapping = {}

    # Create new structure
    for category, items in NEW_STRUCTURE.items():
        category_dir = DEST_DIR / category
        ensure_directory(category_dir)

        for item in items:
            src_path = SRC_DIR / item
            dest_path = category_dir / Path(item).name

            if item.endswith("/"):
                # Handle directories
                dir_name = item.rstrip("/")
                src_dir = SRC_DIR / dir_name
                dest_dir = category_dir / dir_name

                if src_dir.exists() and src_dir.is_dir():
                    print(f"Copying directory {src_dir} to {dest_dir}")
                    shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
                    path_mapping[str(Path(dir_name))] = f"../{category}/{dir_name}"
            else:
                # Handle files
                if src_path.exists() and src_path.is_file():
                    ensure_directory(dest_path.parent)
                    copy_file(src_path, dest_path)
                    path_mapping[item] = f"../{category}/{item}"

    # Update links in all markdown files
    for root, _, files in os.walk(DEST_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = Path(root) / file
                try:
                    with open(file_path, encoding="utf-8") as f:
                        content = f.read()

                    updated_content = update_links(content, path_mapping)

                    if updated_content != content:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(updated_content)
                        print(f"Updated links in {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")


def generate_mkdocs_nav() -> List[Dict]:
    """Generate MkDocs navigation configuration."""
    nav = []

    for category, items in NEW_STRUCTURE.items():
        category_items = []
        category_dir = DEST_DIR / category

        for item in items:
            item_name = Path(item).stem.replace("_", " ").title()
            if item.endswith("/"):
                # Handle directories
                dir_name = item.rstrip("/")
                dir_path = category_dir / dir_name
                if dir_path.exists():
                    sub_items = [
                        {
                            f"{f.stem.replace('_', ' ').title()}": f"{category}/{dir_name}/{f.name}"
                        }
                        for f in sorted(dir_path.glob("*.md"))
                    ]
                    category_items.append({dir_name.title(): sub_items})
            else:
                # Handle files
                file_path = category_dir / Path(item).name
                if file_path.exists():
                    category_items.append({item_name: f"{category}/{item}"})

        nav.append({category.title(): category_items})

    return nav


def main():
    print("Starting documentation migration...")

    # Create backup of current docs
    backup_dir = DOCS_DIR / "backup"
    print(f"Creating backup in {backup_dir}")
    ensure_directory(backup_dir)
    shutil.copytree(SRC_DIR, backup_dir / "docs", dirs_exist_ok=True)

    # Migrate files
    migrate_files()

    # Generate new MkDocs navigation
    nav = generate_mkdocs_nav()

    # Create mkdocs.yml
    mkdocs_config = {
        "site_name": "ReadyAPI",
        "site_url": "https://readyapi.github.io",
        "repo_url": "https://github.com/readyapi/readyapi",
        "docs_dir": "docs/en/docs/new_structure",
        "nav": nav,
        "theme": {
            "name": "material",
            "features": ["navigation.tabs", "navigation.sections", "search.highlight"],
        },
        "markdown_extensions": [
            "toc",
            "tables",
            "fenced_code",
            "codehilite",
            "mdx_include",
            "admonition",
        ],
    }

    with open(DOCS_DIR / "mkdocs.new.yml", "w") as f:
        yaml.dump(mkdocs_config, f, default_flow_style=False, sort_keys=False)

    print("\nMigration complete!")
    print(f"1. Review the new structure in: {DEST_DIR}")
    print(f"2. Check the new mkdocs config: {DOCS_DIR}/mkdocs.new.yml")
    print("3. Test the site with: mkdocs serve -f docs/mkdocs.new.yml")


if __name__ == "__main__":
    main()
