from pathlib import Path
import json
import sys


def main() -> int:
    root = Path(__file__).parent
    fixtures = root / "fixtures"
    files = sorted(fixtures.glob("*.json"))
    if not files:
        print("No fixtures found.")
        return 1

    print(f"Found {len(files)} fixtures:")
    for file in files:
        data = json.loads(file.read_text(encoding="utf-8"))
        print(f"- {file.name}: {', '.join(data.keys())}")

    print("Contract test scaffold only. Replace with real evaluators later.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
