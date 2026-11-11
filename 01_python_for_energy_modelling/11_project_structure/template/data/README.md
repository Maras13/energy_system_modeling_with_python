# Data

Raw downloads go to `raw/`, cleaned model inputs to `processed/`. Both are ignored by Git — the code
re-creates them. This file is the **provenance record**: for every dataset, write down where it came
from so anyone can reproduce your inputs.

| File | Source | Retrieved | Licence | Processing |
|---|---|---|---|---|
| `raw/hr_load_2024.csv` | ENTSO-E Transparency Platform, Actual Total Load, bidding zone HR (`10YHR-HEP------M`) | YYYY-MM-DD | ENTSO-E terms of use | — |
| `processed/hr_load_2024.csv` | from `raw/hr_load_2024.csv` | YYYY-MM-DD | — | UTC, hourly mean, duplicates (keep last), gaps ≤ 3 h interpolated (`hr_energy.data`) |

Replace the example rows with your own datasets.
