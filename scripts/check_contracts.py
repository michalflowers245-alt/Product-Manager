from pathlib import Path
import sys


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1] / "skills"
    files = sorted(skill_dir.glob("*/SKILL.md"))
    missing = []
    for file in files:
        text = file.read_text(encoding="utf-8")
        if "## 必须输出" not in text:
            missing.append(file)

    if missing:
        for file in missing:
            print(f"Missing output contract section: {file}")
        return 1

    print("All skills contain output contract sections.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
