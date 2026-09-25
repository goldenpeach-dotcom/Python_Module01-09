import os


class ConfigError(Exception):
    pass


VALID_MODES = {"development", "production"}

ALL_ENV_KEYS: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

STRICT_REQUIRED_KEYS: list[str] = [
    "DATABASE_URL",
    "API_KEY",
    "ZION_ENDPOINT",
]

ENV_TO_CONFIG: dict[str, str] = {
    "MATRIX_MODE": "mode",
    "DATABASE_URL": "db",
    "API_KEY": "api_key",
    "LOG_LEVEL": "log_level",
    "ZION_ENDPOINT": "zion",
}


def load_config(required_keys: list[str]) -> dict[str, str | None]:
    """
    Check if the .env file exists and load .env
    """
    try:
        from dotenv import load_dotenv
    except ImportError:
        raise ConfigError("python-dotenv is not installed.")

    env_exists = os.path.exists(".env")
    has_inline_env = any(key in os.environ for key in required_keys)

    if not env_exists and not has_inline_env:
        raise ConfigError(
            ".env file is missing and no environment variables are set."
        )

    load_dotenv()

    mode_raw = os.environ.get("MATRIX_MODE")
    log_level_raw = os.environ.get("LOG_LEVEL")
    mode = mode_raw if mode_raw else "development"

    if mode not in VALID_MODES:
        raise ConfigError(
            f"invalid MATRIX_MODE '{mode}', "
            f"must be one of {sorted(VALID_MODES)}"
        )

    config: dict[str, str | None] = {
        "mode": mode,
        "db": os.environ.get("DATABASE_URL"),
        "api_key": os.environ.get("API_KEY"),
        "log_level": log_level_raw if log_level_raw else "INFO",
        "zion": os.environ.get("ZION_ENDPOINT"),
    }

    if not mode_raw:
        print(f"[INFO] MATRIX_MODE not set, using default '{config['mode']}'")
    if not log_level_raw:
        print(
            f"[INFO] LOG_LEVEL not set, using default '{config['log_level']}'"
        )

    missing = [
        env for env in STRICT_REQUIRED_KEYS
        if config[ENV_TO_CONFIG[env]] is None
    ]

    if missing:
        raise ConfigError(f"missing required keys: {', '.join(missing)}")

    if config["mode"] == "production" and not config["api_key"]:
        raise ConfigError("PRODUCTION mode needs API_KEY.")

    return config


def check_hardcoded_secrets(
    required_keys: list[str], filepath: str = "oracle.py"
) -> bool:
    """
    Return True if no secret keys are assigned a quoted string in the file.
    """

    try:
        with open(filepath, "r") as f:
            lines: list[str] = f.readlines()
    except OSError:
        print(
            f"[WARNING] could not read {filepath} "
            "for hardcoded secret check"
        )
        return False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#") or "=" not in stripped:
            continue
        name, _, rest = stripped.partition("=")
        name = name.strip()
        if name in required_keys:
            value = rest.strip()
            if value[:1] in ("'", '"'):
                return False

    return True


def check_env_file_valid(
    required_keys: list[str], env_path: str = ".env"
) -> bool:
    """
    Check if the .env file exists and contains all the required keys.
    """
    if not os.path.exists(env_path):
        return False
    try:
        with open(env_path, "r") as f:
            content: str = f.read()
        return all(key in content for key in required_keys)
    except OSError:
        print(f"[WARNING] could not read {env_path}")
        return False


def check_override_works(original_value: str | None) -> bool:
    """
    Check whether environment variables passed via the command line
    take precedence over those in .env.
    """
    if original_value is None:
        return True
    return os.environ.get("MATRIX_MODE") == original_value


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")


    original_mode: str | None = os.environ.get("MATRIX_MODE")
    try:
        config: dict[str, str | None] = load_config(STRICT_REQUIRED_KEYS)
    except ConfigError as e:
        print(
            f"Oracle cannot continue: {e}"
            "Shutting down...")
        return

    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")
    print(f"Database: {config['db'] or 'Connected to local instance'}")
    print(f"API Access: {'Authenticated' if config['api_key'] else 'Missing'}")
    print(f"Log Level: {config['log_level']} ")
    print(f"Zion Network: {'Online' if config['zion'] else 'Offline'}")

    print("Environment security check:")
    print(
        "[OK] No hardcoded secrets detected"
        if check_hardcoded_secrets(STRICT_REQUIRED_KEYS) else
        "[FAIL] Hardcoded secrets found!"
        )
    print(
        "[OK] .env file properly configured"
        if check_env_file_valid(ALL_ENV_KEYS) else
        "[FAIL] .env file missing or incomplete"
        )
    print(
        "[OK] Production overrides available"
        if check_override_works(original_mode) else
        "[FAIL] Production overrides not working"
        )

    print("\nThe Oracle sees all configurations.")



if __name__ == "__main__":
    main()
