from dataclasses import dataclass
from pathlib import Path

from pydantic_ai import Agent, RunContext


@dataclass
class Deps:
    file_path: Path


lint_fixer = Agent(
    model="ollama:qwen2.5",
    system_prompt="You are a helpful linter that fixes Python code. Provide clear, concise fixes.",
    deps_type=Deps,
)


@lint_fixer.tool
async def read_file(ctx: RunContext[Deps]) -> str:
    """Read the contents of the file that needs fixing."""
    return ctx.deps.file_path.read_text()


@lint_fixer.tool
async def write_file(ctx: RunContext[Deps], content: str) -> None:
    """Write the fixed content back to the file."""
    ctx.deps.file_path.write_text(content)
