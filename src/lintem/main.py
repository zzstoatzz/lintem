import asyncio
import subprocess
from pathlib import Path
from typing import Any, Coroutine

from .agent import Deps, lint_fixer


async def check_files(paths: list[Path]) -> list[tuple[Path, str]]:
    """Run Ruff on the given files and return any lint errors."""
    errors: list[tuple[Path, str]] = []
    for path in paths:
        print(f"Checking {path}")
        buffer = subprocess.run(["ruff", "check", path], capture_output=True, text=True)
        if (stdout := buffer.stdout) == "All checks passed!\n":
            print(f"{stdout} 🎉")
            continue
        print(f"{stdout} 🚨")
        errors.append((path, stdout))
    return errors


async def fix_file(file_path: Path, errors: str) -> None:
    """Fix a single file's lint errors using the AI agent."""
    deps = Deps(file_path=file_path)
    result = await lint_fixer.run(
        f"Fix the following lint errors in {file_path}:\n" + errors,
        deps=deps,
    )
    print(f"Fixed {file_path}: {result.data}")


async def _main() -> None:
    tasks: list[Coroutine[Any, Any, None]] = []
    for file_path, errors in await check_files(list(Path("src").rglob("*.py"))):
        if errors:
            tasks.append(fix_file(file_path, errors))

    await asyncio.gather(*tasks)


def main() -> None:
    asyncio.run(_main())
