"""Load and validate the YAML configuration. Fail early, with a clear message, on bad input."""

from __future__ import annotations

from pathlib import Path

import yaml

REQUIRED_GENERATOR_KEYS = {"carrier", "p_nom", "marginal_cost"}


class ConfigError(ValueError):
    """Raised when the configuration is incomplete or physically implausible."""


def load_config(path: str | Path) -> dict:
    """Read a YAML config file and validate it."""
    with open(path, encoding="utf-8") as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config


def validate_config(config: dict) -> None:
    """Check structure and physical plausibility; raise ConfigError on the first problem."""
    for key in ("name", "snapshots", "load", "generators"):
        if key not in config:
            raise ConfigError(f"missing top-level key: {key!r}")
    if int(config["snapshots"].get("hours", 0)) <= 0:
        raise ConfigError("snapshots.hours must be a positive number of hours")
    for name, gen in config["generators"].items():
        missing = REQUIRED_GENERATOR_KEYS - gen.keys()
        if missing:
            raise ConfigError(f"generator {name!r} is missing {sorted(missing)}")
        if gen["p_nom"] < 0:
            raise ConfigError(f"generator {name!r}: p_nom must be >= 0 MW")
        if not 0 <= gen.get("p_max_pu", 1.0) <= 1:
            raise ConfigError(f"generator {name!r}: p_max_pu must be in [0, 1]")
