"""Build the student tutorial zip from docs/examples.

Run from the repository root:  python scripts/make_zip.py
Creates docs/downloads/lego_spike_tutorials.zip containing:
    lego_spike_tutorials/<page>/<page>_<example>.py

Pybricks keeps every program in one flat list, so each file gets a unique
name made from its page and example folder names.
"""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "docs" / "examples"
OUT = ROOT / "docs" / "downloads" / "lego_spike_tutorials.zip"


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    names = {}
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for main_py in sorted(EXAMPLES.rglob("main.py")):
            # Keep only <page>/<example>, dropping any group level (hub/, motors/ ...)
            page, example = main_py.parent.relative_to(EXAMPLES).parts[-2:]
            name = f"{page}_{example}.py"
            if name in names:
                print(f"WARNING: {name} is made by both {names[name]} and {main_py}")
            names[name] = main_py
            zf.write(main_py, Path("lego_spike_tutorials", page, name))
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(names)} programs)")


if __name__ == "__main__":
    main()
