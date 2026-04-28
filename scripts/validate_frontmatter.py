from pathlib import Path
import sys


REQUIRED = ("name:", "description:", "license:")


def main() -> int:
    root = Path(__file__).resolve().parents[1] / "skills"
    skill_files = sorted(root.glob("*/SKILL.md"))
    if not skill_files:
        print("No SKILL.md files found.")
        return 1

    failed = []
    for file in skill_files:
        text = file.read_text(encoding="utf-8")
        for token in REQUIRED:
            if token not in text:
                failed.append((file, token))

    if failed:
        for file, token in failed:
            print(f"Missing {token} in {file}")
        return 1

    print(f"Validated {len(skill_files)} skill manifests.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
