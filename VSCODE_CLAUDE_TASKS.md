# Tasks for Claude in VS Code

These tasks finish the Zensical rework of *Lego Spike Python Coding*. They couldn't be done from Cowork, which could only create and overwrite files in this folder. It couldn't delete files, run git, access GitHub or write inside `.github/`.

Work on the `zensical` branch. Do the tasks in order, and check with Damien before each one marked **Confirm first**. Report the output of the checks after each task.

## Context

- **Site generator:** Zensical 0.0.66 (pinned in `requirements.txt`). Config is `zensical.toml`. Pages are in `docs/`.
- **Preview:** `zensical serve` (http://localhost:8000). **Build:** `zensical build --clean` (must report `No issues found`).
- **Audience:** Year 8 students (AC v9 Digital Technologies 7–8).
- **Hardware and software:** LEGO SPIKE Prime hub running the latest Pybricks firmware, programmed in the Pybricks IDE (code.pybricks.com). The class robot is fixed:
    - left motor Port E (`Direction.COUNTERCLOCKWISE`), right motor Port F (`Direction.CLOCKWISE`)
    - force sensor Port B, ultrasonic (distance) sensor Port C, colour sensor Port D
    - `DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)`
    - hub mounted flat, light matrix facing up
- **Folder layout:**
    - `docs/<section>/<page>.md` with sections `start`, `hub`, `motors`, `drivebase`, `sensors`, `planning`, `reference`
    - examples: `docs/examples/<group>/<page>/<example>/main.py`, included with `--8<-- "examples/..."` (pymdownx.snippets, base path `docs`)
    - exercise starters: `docs/examples/<group>/<page>/exN_name/main.py`
    - solutions: `docs/solutions/<group>/<page>/exN_name.py`
    - images: `docs/assets/`; stylesheet: `docs/stylesheets/extra.css`
    - student zip: `docs/downloads/lego_spike_tutorials.zip` (git-ignored, built by `scripts/make_zip.py`)
- **Scripts:**
    - `python scripts/make_zip.py` builds the zip. Pybricks keeps programs in one flat list, so each file is named `<page>_<example>.py` inside a page folder. Expected: `Wrote docs/downloads/lego_spike_tutorials.zip (129 programs)` and no `WARNING` lines.
    - `python scripts/check_explanations.py` checks every Code explanation against its example. Expected: `0 issue(s) found`.
    - `python scripts/update_starters.py` copies each exercise's wording from its page into the comment block at the top of its starter file. Run it after changing any exercise wording.
- **Colour scheme** (from the LEGO Education SPIKE Prime Element Overview, set in `docs/stylesheets/extra.css`):
    - LEGO magenta `#923978`: top bar, tabs, links, headings (light mode); magenta tint `#d46aa8`: links (dark mode)
    - LEGO yellow `#ffcf00`: active tab, headings (dark mode), tip callouts
    - SPIKE teal `#0ab8d3`: PRIMM callouts
    - LEGO green `#00852b` (dark mode `#4cb86b`): Code explanation (note) callouts
    - red tint `#ee4b52`: warning callouts
    - Magenta is never used for callouts.
- **Example rules:** every file starts with the full Pybricks template imports (add `, Icon` to line 3 when needed). Each example uses its method once, with only the supporting code needed to see it work, and keeps the `# Setup` / `# Main loop` structure. Comments are structural only (`# Setup`, `# Main loop`, `# Input`, `# Process`, `# Output`). If an example changes, update its code explanation and run the checker.
- **Page templates:**
    - device pages (hub, motors, drive base, sensors): one-sentence description → "Possible uses:" list → Connect it → Set it up → Methods table → for each method: explanation, example, PRIMM callout, collapsible `??? note "Code explanation"` → Documentation (standard sentence) → Exercises
    - lesson pages (Program Structure, Gyro Driving): concept sections, each with an example, PRIMM and a code explanation, then Exercises
    - project page (Developing Robot Code): What you need → Plan → Build it → Test it → Extend it
    - guide pages (Setup, Calibration, Flowcharts): short sections with numbered steps (step, why, expected result)
- **Writing style:** Australian English for Year 8, in Damien's voice:
    - an inclusive "we" voice ("we need to", "our program", "Let's"); code explanations in the third person
    - bold new terms the first time they are used
    - PRIMM callout after every example: `!!! primm "PRIMM"` with "1. **Predict** what you think will happen. Be specific. 2. **Run** the program. 3. Time to **investigate** the code. What does each line do?"
    - code explanations as `- **line n** → full sentence starting with a lower-case verb and ending in a full stop.`, with `…` joining an `if` and its `else`
    - exercises start with a PRIMM callout ("Time to **modify** the code and see what happens.") and are phrased as questions ("Can you …?"); explain-why exercises ask "What happens if …? Why do you think this happens?"
    - code uses Pybricks' American spellings (`Color`, `ColorSensor`), prose uses "colour", and our variables use `colour_sensor`
- **Rework plan:** the audit and plan are in Damien's Claude project as `claude/lego-spike-tutorials_rework_plan.md`.

## 1. Restore the original images

When Cowork copied the images into `docs/assets/`, a metadata block was added to each PNG. The originals are still in the root `assets/` folder.

1. For every file in `docs/assets/` that also exists in `assets/`, copy the `assets/` version over the `docs/assets/` version. Also copy `spike_logo.png` and `spike_logo.ico` from the root over `docs/assets/`.
2. Check with `git diff --stat docs/assets` that only image files changed.
3. Run `zensical build --clean`. Expected: `No issues found`.

Do this before task 3, which deletes `assets/`.

## 2. Delete unused files in `docs/` — Confirm first

These are not used by any page:

- `docs/assets/create_new_project.png`
- `docs/assets/flowchart_symbols.png`

Keep `docs/assets/diagrams.drawio`. It is the editable source of the flowchart images.

Before deleting, search the repo to confirm neither file is referenced. Then run `zensical build --clean`.

## 3. Remove the old Sphinx site — Confirm first

The old site is still on `main` and will be tagged before merging (task 7), so nothing is lost. Show Damien this list before deleting:

- `01_setup.md` to `12_flowcharts.md` and `99_examples.md` (all numbered pages in the root)
- `index.md` (root only; the new home page is `docs/index.md`)
- `conf.py`, `Makefile`, `make.bat`
- `_build/`, `_static/`, `_templates/`
- `assets/` (after task 1), `python_files/`
- `%GIT%lego-spike-tutorials/` (a stray chat history database)
- `TODO.md` (every item is now covered by the new site)
- `spike_logo.ico`, `spike_logo.png` in the root (copies are in `docs/assets/`)

Keep `README.md`, `.gitignore`, `.gitattributes`, `requirements.txt`, `zensical.toml`, `VSCODE_CLAUDE_TASKS.md`, `docs/`, `scripts/`, `.github/` and Damien's local `.venv/`.

Add `_build/` to `.gitignore` so it can't be committed again. Then run `zensical build --clean`.

## 4. Replace the deploy workflow

Delete `.github/workflows/write_to_gh_pages.yml` and create `.github/workflows/deploy.yml` with the workflow below. It builds the student zip, builds the site with Zensical and deploys with GitHub Pages Actions. It only runs on `main`, so pushing to `zensical` won't change the live site.

The zip is git-ignored, so the `make_zip.py` step is required. Without it, the download link on the live site would be broken.

```yaml
name: Deploy site

# Runs only when changes are pushed to main
on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/configure-pages@v6
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v6
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - run: python scripts/make_zip.py
      - run: zensical build --clean
      - uses: actions/upload-pages-artifact@v5
        with:
          path: site
      - uses: actions/deploy-pages@v5
        id: deployment
```

The action versions come from Zensical's own template. Confirm each version exists on GitHub before committing.

## 5. Update `README.md`

Replace the Sphinx-era README with:

- what the site is and who it is for (Year 8 students, LEGO SPIKE Prime, Pybricks)
- the live URL: https://damom73.github.io/lego-spike-tutorials/
- how to preview it (`pip install -r requirements.txt`, then `zensical serve`)
- how to rebuild the student zip (`python scripts/make_zip.py`)
- how to check explanations (`python scripts/check_explanations.py`) and update starter comments (`python scripts/update_starters.py`)
- the folder layout from the Context section above
- the licences: GPLv3 for code, CC BY-NC-SA 4.0 for content (this replaces the old MIT statement)

Also add a `LICENSE` file with the GPLv3 text if Damien agrees. **Confirm first.**

## 6. Final checks

1. Run `python scripts/make_zip.py`. Expected: 129 programs, no warnings.
2. Run `python scripts/update_starters.py`. Expected: `0 starter file(s) updated`.
3. Run `python scripts/check_explanations.py`. Expected: `0 issue(s) found`.
4. Run `zensical build --clean`. Expected: `No issues found`.
5. Check that every external link in `docs/` returns a working page, especially the `docs.pybricks.com` links. Report broken ones to Damien rather than guessing replacements.
6. Spell-check the pages for Australian English (ignoring code and Pybricks names such as `Color`).
7. Commit to `zensical` and push.

## 7. Go live — Confirm first

1. Tag the current `main` as `v1-sphinx` and push the tag, so the old site can be restored.
2. Merge `zensical` into `main` and push.
3. Change the Pages source to GitHub Actions: in the repo go to **Settings** → **Pages** → **Source**, or run `gh api -X PUT repos/damom73/lego-spike-tutorials/pages -f build_type=workflow`.
4. Watch the **Deploy site** workflow run, then check that https://damom73.github.io/lego-spike-tutorials/ shows the new site and that the tutorial zip downloads.
5. Once the new site is confirmed working, the old `gh-pages` branch can be deleted. **Confirm first.**

## Tasks for Damien (not for Claude)

Run the examples and solutions on a class robot, and check these in particular:

- **Setup**
    - `check_config` prints ports B to F in order, turns 360° clockwise and drives 100 mm
    - the Pybricks IDE button names on the Setup page ("Create a new file", "Import a file") match the current IDE
- **Hub**
    - `blink()` and `animate()` keep running in the background with `while True: pass`
    - Status Light Exercise 2: the SOS timings look right
    - Light Matrix: `number()` shows `>` after 99
    - Speaker: `volume(20)` is audible; *Saints* sounds right at tempo 180
    - IMU: heading is positive when the robot turns clockwise; the spirit-level threshold (3°) works
- **Motors**
    - the left motor's positive direction drives forwards
    - `track_target()` looks different from `run_target()`
    - `load()` gives sensible values at 300 deg/s
    - Motor as a Sensor Exercise 3: the robot reverses when stalled (500 ms grace)
- **Drive Base**
    - `arc()` with a positive radius curves right
    - `settings(straight_speed=400)` works with a keyword
    - Drive Base as a Sensor Exercise 3: the angle is positive when the robot is turned right by hand
    - Gyro Driving: the gyro square finishes closer to the start; `hold_heading` corrects when pushed; `face_start` returns to the starting direction
    - Calibration: the example adjustments (55.5 mm, 81 mm) are sensible step sizes
- **Sensors**
    - Colour: `color()` and `reflection()` turn the sensor lights on by themselves and `ambient()` turns them off (the tip on the Colour page says so)
    - Colour exercise thresholds: night light `10`, stop on line `20`
    - Distance: the closest reliable reading and the 2000 mm limit match the warning box
    - Distance: which lights `lights.on([100, 0, 100, 0])` turns on
    - Force: the `pressed(5)` threshold feels right
- **Planning**
    - `from urandom import randint` works, and move-and-avoid stops before obstacles at 100 mm
- **Decisions**
    - whether the planning page's Extend it challenges should become numbered exercises with solutions
    - photos or GIFs of the class robot for the Setup page and exercise targets
