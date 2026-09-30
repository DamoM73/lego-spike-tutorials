"""Copy each exercise's wording from its page into the top of its starter file.

Run from the repository root:  python scripts/update_starters.py

For every "### Exercise N" section with a "Starter: `page/exN_name`" line, the
exercise text is turned into a comment block (markdown removed, wrapped at
76 characters) and replaces any comment block already at the top of
docs/examples/.../<page>/<exN_name>/main.py.
"""
from pathlib import Path
import re
import textwrap

DOCS = Path(__file__).resolve().parent.parent / "docs"
EXAMPLES = DOCS / "examples"


def plain(text):
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)          # images
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)      # links
    text = text.replace("**", "").replace("`", "")
    return text


def comment_block(title, body):
    lines = [f"# {title}"]
    for para in plain(body).strip().split("\n"):
        para = para.rstrip()
        if not para.strip() or para.strip() in ("For example:",):
            continue
        indent = "  " if para.lstrip().startswith("- ") else ""
        wrapped = textwrap.wrap(para.strip(), 76, subsequent_indent=indent)
        lines += [f"# {w}" for w in wrapped]
    return "\n".join(lines) + "\n#\n\n"


def main():
    updated = 0
    for md in sorted(DOCS.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for m in re.finditer(r"^### (Exercise \d+)\n(.*?)(?=^##|\Z)", text, re.S | re.M):
            title, section = m.groups()
            starter = re.search(r"^Starter: `([^`]+)`", section, re.M)
            if not starter:
                continue
            body = section[starter.end():]
            matches = [p for p in EXAMPLES.rglob("main.py")
                       if p.parent.relative_to(EXAMPLES).as_posix().endswith(starter.group(1))]
            if len(matches) != 1:
                print(f"WARNING  {md.relative_to(DOCS)}  {title}: found {len(matches)} starters for {starter.group(1)}")
                continue
            path = matches[0]
            code = path.read_text(encoding="utf-8")
            code = re.sub(r"\A(#.*\n)+\n*", "", code) if code.startswith("# Exercise") else code
            new = comment_block(title, body) + code
            if new != path.read_text(encoding="utf-8"):
                path.write_text(new, encoding="utf-8")
                updated += 1
    print(f"{updated} starter file(s) updated")


if __name__ == "__main__":
    main()
