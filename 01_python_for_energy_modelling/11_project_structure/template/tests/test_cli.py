import json

from hr_energy.cli import main
from conftest import ROOT


def test_cli_writes_results(tmp_path):
    summary = main(["--config", str(ROOT / "config" / "config.yaml"), "--out", str(tmp_path)])
    out = tmp_path / "base"
    for name in ["dispatch_MW.csv", "price_EUR_per_MWh.csv", "summary.json"]:
        assert (out / name).is_file(), name
    assert json.loads((out / "summary.json").read_text())["total_cost_EUR"] == summary["total_cost_EUR"]
