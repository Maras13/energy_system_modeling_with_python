import pytest

from hr_energy.config import ConfigError, validate_config


def test_base_config_is_valid(config):
    validate_config(config)


def test_missing_section_is_rejected(config):
    del config["load"]
    with pytest.raises(ConfigError, match="load"):
        validate_config(config)


def test_negative_capacity_is_rejected(config):
    config["generators"]["coal"]["p_nom"] = -10
    with pytest.raises(ConfigError, match="coal"):
        validate_config(config)


def test_availability_above_one_is_rejected(config):
    config["generators"]["hydro_ror"]["p_max_pu"] = 1.5
    with pytest.raises(ConfigError, match="p_max_pu"):
        validate_config(config)
