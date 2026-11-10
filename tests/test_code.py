"""Every script runs clean, passes its own checks, and prints the published output."""
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPTS = sorted((ROOT / "code").glob("*.py"))


def run(script):
    return subprocess.run([sys.executable, str(script)], capture_output=True, text=True,
                          encoding="utf-8", timeout=120)


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda p: p.name)
def test_runs_and_passes_its_own_checks(script):
    result = run(script)
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda p: p.name)
def test_output_matches_what_was_published(script):
    expected = (ROOT / "tests" / "expected" / f"{script.stem}.txt").read_text(encoding="utf-8")
    assert run(script).stdout.split() == expected.split()


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda p: p.name)
def test_is_deterministic(script):
    assert run(script).stdout == run(script).stdout


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda p: p.name)
def test_states_its_basis_and_checks_itself(script):
    source = script.read_text(encoding="utf-8")
    assert source.lstrip().startswith('"""'), "missing module docstring"
    assert "assert " in source, "missing hand-calculation check"


def test_readme_links_point_at_real_files():
    import re
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    targets = re.findall(r"\]\((?!https?:)([^)#]+)\)", readme)
    assert targets
    for target in targets:
        assert (ROOT / target).exists(), target
