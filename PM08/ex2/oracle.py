import os
import re
from dotenv import load_dotenv


class ConfigError(Exception):
    pass


def load_config() -> dict[str, str | None]:

    env_exists = os.path.exists(".env")

    has_inline_env = "MATRIX_MODE" in os.environ or "API_KEY" in os.environ

    if not env_exists and not has_inline_env:
        raise ConfigError(".env file is missing and no environment variables are set.")

    load_dotenv()

    config: dict[str, str | None] = {
        "mode": os.environ.get("MATRIX_MODE", "development"),
        "db": os.environ.get("DATABASE_URL"),
        "api_key": os.environ.get("API_KEY"),
        "log_level": os.environ.get("LOG_LEVEL", "INFO"),
        "zion": os.environ.get("ZION_ENDPOINT"),
    }

    missing = [k for k, v in config.items() if v is None]
    if missing:
        raise ConfigError(f"missing required keys: {', '.join(missing)}")

    if config["mode"] == "production":
        if not config["api_key"]:
            raise ConfigError("PRODUCTION mode needs API_KEY.")

    return config


def check_hardcoded_secrets(filepath="oracle.py") -> bool:

    try:
        with open(filepath, "r") as f:
            code: str = f.read()
            pattern: str = r'(API_KEY|SECRET|PASSWORD)\s*=\s*["\'][^"\']+["\']'
            suspicious: list[str] = re.findall(pattern, code)
        return len(suspicious) == 0
    except (FileNotFoundError, PermissionError, OSError):
        print(
            f"[WARNING] could not read {filepath}"
            "for checking hardcoded secret check"
        )
        return False


def check_env_file_valid(required_keys: list[str], env_path=".env"):
    """.envファイルが存在し、必須キーが揃っているかチェック"""
    if not os.path.exists(env_path):
        return False
    try:
        with open(env_path, "r") as f:
            content = f.read()
        return all(key in content for key in required_keys)
    except (OSError):
        print(f"[WARNING] could not read {env_path}")
        return False


def check_override_works(test_key="MODE"):
    """OS環境変数が.envより優先されるかチェック"""
    os.environ[test_key] = "production_override_test"
    load_dotenv(override=False)  # .envの値でOS環境変数を潰さない設定
    result = os.environ.get(test_key) == "production_override_test"
    return result



def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    try:
        config = load_config()
    except ConfigError as e:
        print(f"[ERROR] {e}")
        print("Oracle cannot continue. Shutting down...")
        return

    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")
    print(f"Database: {config['db'] or 'Connected to local instance'}")
    print(f"API Access: {'Authenticated' if config['api_key'] else 'Missing'}")
    print(f"Log Level: {config['log_level'] or 'Missing'} ")
    print(f"Zion Network: {config['zion'] or 'Offline'}")

    # security_check(config)

    print("Environment security check:")
    required_keys: list[str] = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    print("[OK] No hardcoded secrets detected" if check_hardcoded_secrets()
          else "[FAIL] Hardcoded secrets found!")
    print("[OK] .env file properly configured" if check_env_file_valid(required_keys)
          else "[FAIL] .env file missing or incomplete")
    print("[OK] Production overrides available" if check_override_works()
          else "[FAIL] Production overrides not working")


    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
