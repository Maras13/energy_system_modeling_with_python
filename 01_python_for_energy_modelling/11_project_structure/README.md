# 11 Reproducible energy modelling projects

| Item | Lesson | Content |
|---|---|---|
| `01_reproducible_projects.ipynb` | M1.6 | Project anatomy (src layout), every number in a validated YAML config, tests that check physics and economics, mutation testing (a test must compare against an independent source), a command-line entry point, environments, secrets and data provenance, a README that gets read |
| [`template/`](template/) | — | A working project: the package `hr_energy` (config, data, model, CLI), 14 pytest tests, config, data provenance, README skeleton. **Copy it to start portfolio project P1.** |
| [`../PROJECT_P1.md`](../PROJECT_P1.md) | P1 | The brief for your first portfolio project |

Exercises are in `exercise/`, the answer key in `exercise/solutions/` (submit your own answers first).
The exercise builds scenario tooling on the template and an `audit_project` checker to run on your P1 repo.

## Using the template
```bash
cp -r template ~/projects/hr-energy && cd ~/projects/hr-energy && git init
pip install -e ".[dev]"          # or: conda env create -f environment.yml
pytest                           # 14 tests, all must pass
python -m hr_energy --config config/config.yaml --out results/
```
Tested with Python 3.12, PyPSA 1.4.0, HiGHS 1.15, pandas 3.0, pytest 9.2.
