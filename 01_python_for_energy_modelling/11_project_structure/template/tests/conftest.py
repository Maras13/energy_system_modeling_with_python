from pathlib import Path

import pytest

from hr_energy.config import load_config

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def config():
    """A fresh copy of the base configuration for every test."""
    return load_config(ROOT / "config" / "config.yaml")
