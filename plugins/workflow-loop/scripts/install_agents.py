#!/usr/bin/env python3
"""Install Workflow Loop's optional native Codex roles (Python 3.11+)."""

import argparse
import os
from pathlib import Path
import shutil
import tempfile
import tomllib


def main() -> None:
    codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--agents-dir", type=Path, default=codex_home / "agents",
        help="Destination (default: $CODEX_HOME/agents or ~/.codex/agents).",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing.")
    parser.add_argument(
        "--replace", action="store_true",
        help="Back up and replace differing definitions; otherwise refuse conflicts.",
    )
    args = parser.parse_args()
    destination = args.agents_dir.expanduser().absolute()
    source = Path(__file__).resolve().parents[1] / "agents"
    pending = []
    conflicts = []

    # Preflight every role before creating a directory or installing any files.
    for name in ("planner", "implementer", "reviewer"):
        original = source / f"{name}.toml"
        content = original.read_bytes()
        definition = tomllib.loads(content.decode("utf-8"))
        if definition.get("name") != name or any(
            not isinstance(definition.get(key), str) or not definition[key].strip()
            for key in ("description", "developer_instructions")
        ):
            parser.error(f"Invalid bundled agent: {original}")
        target = destination / original.name
        if target.is_symlink() or (target.exists() and not target.is_file()):
            parser.error(f"Refusing a symlink or non-file destination: {target}")
        if target.exists() and target.read_bytes() == content:
            print(f"Unchanged: {target}")
            continue
        if target.exists() and not args.replace:
            conflicts.append(str(target))
        pending.append((original, target))

    if conflicts:
        parser.error(
            "Existing definitions differ; no files changed. Use --replace to back them up "
            "and replace them:\n" + "\n".join(conflicts)
        )
    if args.dry_run:
        for _, target in pending:
            action = "Back up and replace" if target.exists() else "Install"
            print(f"Would {action.lower()}: {target}")
        return
    if not pending:
        return

    destination.mkdir(parents=True, exist_ok=True)
    for original, target in pending:
        if target.exists():
            descriptor, backup_name = tempfile.mkstemp(
                prefix=f"{target.name}.", suffix=".bak", dir=destination,
            )
            os.close(descriptor)
            shutil.copy2(target, backup_name)
            print(f"Backup: {backup_name}")
        shutil.copy2(original, target)
        print(f"Installed: {target}")
    print("Start a new Codex session with workflow-loop enabled to use these roles.")


if __name__ == "__main__":
    main()
