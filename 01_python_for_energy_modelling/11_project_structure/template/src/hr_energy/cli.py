"""Command line: run the model from a config file and write results.

    python -m hr_energy --config config/config.yaml --out results/
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .config import load_config
from .model import build_network, solve, summarise


def main(argv: list[str] | None = None) -> dict:
    parser = argparse.ArgumentParser(description="Run the hr_energy dispatch model.")
    parser.add_argument("--config", default="config/config.yaml", help="YAML config file")
    parser.add_argument("--out", default="results", help="output directory")
    args = parser.parse_args(argv)

    config = load_config(args.config)
    n = solve(build_network(config), config.get("solver", "highs"))
    summary = summarise(n)

    out = Path(args.out) / config["name"]
    out.mkdir(parents=True, exist_ok=True)
    n.generators_t.p.to_csv(out / "dispatch_MW.csv")
    n.buses_t.marginal_price.to_csv(out / "price_EUR_per_MWh.csv")
    (out / "summary.json").write_text(json.dumps(summary, indent=2))
    print(f"{config['name']}: total cost {summary['total_cost_EUR']:,.0f} EUR, "
          f"mean price {summary['mean_price_EUR_per_MWh']:.1f} EUR/MWh -> {out}")
    return summary
