import os
import sys

VALID_MODES:set[str] = {"development", "production"}

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

try:
    from dotenv import load_dotenv
except ImportError:
    print("ORACLE STATUS: python-dotenv is not installed.")
    print("Install it inside a virtual environment:")
    print("    python3 -m venv matrix_env")
    print("    source matrix_env/bin/activate")
    print("    pip install python-dotenv")
    sys.exit(1)

def resolve_mode() -> str:
    """
    Check the value of MATRIX_MODE
    return:
        the value of MATRIX_MODE
    """

    value = os.environ.get("MATRIX_MODE")
    if not value:
        print("[INFO] MATRIX_MODE not set, using default 'development'")
        return "development"
    if value not in VALID_MODES:
        print(f"[WARNING] invalid MATRIX_MODE '{value}', "
              f"must be one of {sorted(VALID_MODES)}; using default 'development'")
        return "development"
    return value

def load_config() -> dict[str, str | None]:
    """
    Check if the .env file exists and load .env
    """

    load_dotenv()

    config: dict[str, str | None] = {
        name: os.environ.get(name, "") for name in ALL_ENV_KEYS
    }

    config["MATRIX_MODE"] = resolve_mode()

    if not config["LOG_LEVEL"]:
        print("[INFO] LOG_LEVEL not set, using default 'INFO'")
        config["LOG_LEVEL"] = "INFO"
    return config


def describe(config: dict[str, str]) -> list[str]:
    """
    Show the status of environment variables
    param:
        environment variables:dict[str, str]
    return:
        the status of environment variables: list[str]
    """
    return [
        f"Mode: {config['MATRIX_MODE']}",
        f"Database: {config['DATABASE_URL'] or 'Connected to local instance'}",
        f"API Access: {'Authenticated' if config['API_KEY'] else 'Missing'}",
        f"Log Level: {config['LOG_LEVEL']}",
        f"Zion Network: {'Online' if config['ZION_ENDPOINT'] else 'Offline'}",
    ]


def missing_keys(config: dict[str, str]) -> list[str]:
    """
    Find missing environment variable

    param:
        environment variables:dict[str, str]
    return:
        missing environment variables: list[str]
    """
    return [key for key in STRICT_REQUIRED_KEYS if not config[key]]


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
    except OSError:
        print(f"[WARNING] could not read {env_path}")
        return False

    return all(key in content for key in required_keys)


def check_override_works(
    config: dict[str, str],
    original_mode: str | None
) -> bool:
    """
    Check whether environment variables passed via the command line
    take precedence over those in .env.
    """
    if original_mode is None:
        return True
    return config["MATRIX_MODE"] == original_mode

def security_check(config: dict[str, str], original_mode: str | None) -> None:
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected"
          if check_hardcoded_secrets(STRICT_REQUIRED_KEYS)
          else "[FAIL] Hardcoded secrets found!")
    print("[OK] .env file properly configured"
          if check_env_file_valid(ALL_ENV_KEYS)
          else "[FAIL] .env file missing or incomplete")
    print("[OK] Production overrides available"
          if check_override_works(config, original_mode)
          else "[FAIL] Production overrides not working")



def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    original_mode: str | None = os.environ.get("MATRIX_MODE")

    config = load_config()

    if config["MATRIX_MODE"] == "production" and not config["API_KEY"]:
        print("Oracle cannot continue: PRODUCTION mode needs API_KEY.")
        return

    print("Configuration loaded:")
    for line in describe(config):
        print(line)

    security_check(config, original_mode)

    missing: list[str] = missing_keys(config)
    if missing:
        print("\nOracle is troubled. Missing configuration:")
        for key in missing:
            print("-" + key)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
