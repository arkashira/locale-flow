import os
import pytest

from locale_flow import load_config, LocaleFlowConfig


def test_load_config_happy_path():
    env = {
        "LOCALE_FLOW_API_KEY": "test-key",
        "LOCALE_FLOW_ENDPOINT": "https://api.locale-flow.com",
        "LOCALE_FLOW_TIMEOUT": "45",
    }
    cfg = load_config(env)
    assert isinstance(cfg, LocaleFlowConfig)
    assert cfg.api_key == "test-key"
    assert cfg.endpoint == "https://api.locale-flow.com"
    assert cfg.timeout == 45


def test_load_config_default_timeout():
    env = {
        "LOCALE_FLOW_API_KEY": "key",
        "LOCALE_FLOW_ENDPOINT": "https://example.com",
    }
    cfg = load_config(env)
    assert cfg.timeout == 30  # default


def test_load_config_missing_api_key():
    env = {
        "LOCALE_FLOW_ENDPOINT": "https://example.com",
    }
    with pytest.raises(KeyError, match="LOCALE_FLOW_API_KEY"):
        load_config(env)


def test_load_config_missing_endpoint():
    env = {
        "LOCALE_FLOW_API_KEY": "key",
    }
    with pytest.raises(KeyError, match="LOCALE_FLOW_ENDPOINT"):
        load_config(env)


def test_load_config_invalid_timeout():
    env = {
        "LOCALE_FLOW_API_KEY": "key",
        "LOCALE_FLOW_ENDPOINT": "https://example.com",
        "LOCALE_FLOW_TIMEOUT": "-5",
    }
    with pytest.raises(ValueError, match="LOCALE_FLOW_TIMEOUT"):
        load_config(env)


def test_load_config_nonint_timeout():
    env = {
        "LOCALE_FLOW_API_KEY": "key",
        "LOCALE_FLOW_ENDPOINT": "https://example.com",
        "LOCALE_FLOW_TIMEOUT": "abc",
    }
    with pytest.raises(ValueError, match="LOCALE_FLOW_TIMEOUT"):
        load_config(env)
