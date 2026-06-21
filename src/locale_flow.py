import os
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class LocaleFlowConfig:
    api_key: str
    endpoint: str
    timeout: int = 30  # default timeout in seconds


def load_config(env: Dict[str, str] | None = None) -> LocaleFlowConfig:
    """
    Load configuration for Locale‑Flow from environment variables.

    Parameters
    ----------
    env : dict or None
        Optional dictionary to override os.environ (useful for tests).

    Returns
    -------
    LocaleFlowConfig
        Configuration object with validated values.

    Raises
    ------
    KeyError
        If required environment variables are missing.
    ValueError
        If timeout is not a positive integer.
    """
    if env is None:
        env = os.environ

    try:
        api_key = env["LOCALE_FLOW_API_KEY"]
    except KeyError as exc:
        raise KeyError("Missing required environment variable: LOCALE_FLOW_API_KEY") from exc

    try:
        endpoint = env["LOCALE_FLOW_ENDPOINT"]
    except KeyError as exc:
        raise KeyError("Missing required environment variable: LOCALE_FLOW_ENDPOINT") from exc

    timeout_str = env.get("LOCALE_FLOW_TIMEOUT", "30")
    try:
        timeout = int(timeout_str)
        if timeout <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("LOCALE_FLOW_TIMEOUT must be a positive integer") from None

    return LocaleFlowConfig(api_key=api_key, endpoint=endpoint, timeout=timeout)


def get_default_config() -> LocaleFlowConfig:
    """
    Return a default configuration using environment variables.
    """
    return load_config()
