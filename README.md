# Lego Spike Python Coding

Python tutorials for Year 8 students (AC v9 Digital Technologies 7–8) learning to program the LEGO SPIKE Prime robot. The hub runs the [Pybricks](https://pybricks.com/) firmware and students write their code in the Pybricks IDE at [code.pybricks.com](https://code.pybricks.com/).

**Live site:** https://damom73.github.io/lego-spike-tutorials/

The site is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages by `.github/workflows/deploy.yml` whenever changes are pushed to `main`.

## Preview the site

```bash
pip install -r requirements.txt
zensical serve
```

Then open http://localhost:8000. To check a full build, run `zensical build --clean`. It should report `No issues found`.

## Scripts

| Command | What it does |
|---|---|
| `python scripts/make_zip.py` | Builds the student zip `docs/downloads/lego_spike_tutorials.zip`. Each program is named `<page>_<example>.py` inside a page folder, because Pybricks keeps programs in one flat list. The zip is git-ignored and is rebuilt by the deploy workflow. |
| `python scripts/check_explanations.py` | Checks every Code explanation against its example. It should report `0 issue(s) found`. |
| `python scripts/update_starters.py` | Copies each exercise's wording from its page into the comment block at the top of its starter file. Run it after changing any exercise wording. |

## Folder layout

| Path | Contents |
|---|---|
| `zensical.toml` | Site configuration and navigation |
| `docs/<section>/<page>.md` | Pages, in the sections `start`, `hub`, `motors`, `drivebase`, `sensors`, `planning` and `reference` |
| `docs/examples/<group>/<page>/<example>/main.py` | Examples, included in pages with `--8<-- "examples/..."` |
| `docs/examples/<group>/<page>/exN_name/main.py` | Exercise starter files |
| `docs/solutions/<group>/<page>/exN_name.py` | Exercise solutions |
| `docs/assets/` | Images (`diagrams.drawio` is the editable source of the flowchart images) |
| `docs/stylesheets/extra.css` | LEGO colour scheme |
| `docs/downloads/` | Student zip (built by `scripts/make_zip.py`) |
| `scripts/` | Maintenance scripts |

## Licence

- **Code** (examples, starters, solutions and scripts) is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).
- **Content** (tutorial text and images) is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
