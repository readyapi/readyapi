import subprocess
import sys
from unittest.mock import patch

import pytest
import readyapi.cli


def test_readyapi_cli():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "coverage",
            "run",
            "-m",
            "readyapi",
            "dev",
            "non_existent_file.py",
        ],
        capture_output=True,
        encoding="utf-8",
    )
    assert result.returncode == 1, result.stdout
    assert "Path does not exist non_existent_file.py" in result.stdout


def test_readyapi_cli_not_installed():
    with patch.object(readyapi.cli, "cli_main", None):
        with pytest.raises(RuntimeError) as exc_info:
            readyapi.cli.main()
        assert "To use the readyapi command, please install" in str(exc_info.value)
