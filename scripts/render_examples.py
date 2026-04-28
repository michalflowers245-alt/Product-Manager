from pathlib import Path


def main() -> int:
    docs_dir = Path(__file__).resolve().parents[1] / "docs" / "examples"
    rendered_dir = Path(__file__).resolve().parents[1] / "docs" / "examples-rendered"
    rendered_dir.mkdir(parents=True, exist_ok=True)

    for file in docs_dir.glob("*.md"):
        target = rendered_dir / file.name
        target.write_text(file.read_text(encoding="utf-8"), encoding="utf-8")

    print("Rendered example scaffolds.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
