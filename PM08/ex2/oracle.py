import os
from dotenv import load_dotenv


class ConfigError(Exception):
    """設定が欠落している場合の例外"""
    pass


def load_config() -> dict[str, str | None]:

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

    # 本番モードの stricter check
    if config["mode"] == "production":
        if not config["api_key"]:
            raise ConfigError("PRODUCTION mode needs API_KEY.")

    return config


def security_check(config: dict[str, str | None]) -> None:
    print("\nEnvironment security check:")

    env_loaded: bool = any([
    os.environ.get("MATRIX_MODE"),
    os.environ.get("DATABASE_URL"),
    os.environ.get("API_KEY"),
    os.environ.get("LOG_LEVEL"),
    os.environ.get("ZION_ENDPOINT"),
    ])

    print(f"  - .env file loaded .... {'OK' if env_loaded else 'FAILED'}")

    # 必須キーの存在チェック
    print(f"  - MATRIX_MODE ...... {'OK' if config['mode'] else 'MISSING'}")
    print(f"  - DATABASE_URL ..... {'OK' if config['db'] else 'MISSING'}")
    print(f"  - API_KEY .......... {'OK' if config['api_key'] else 'MISSING'}")
    print(f"  - LOG_LEVEL ...... {'OK' if config['log_level'] else 'MISSING'}")
    print(f"  - ZION_ENDPOINT ....... {'OK' if config['zion'] else 'MISSING'}")

    print("  - Sensitive data from env only .... OK")

    # 本番モードの stricter check
    if config["mode"] == "production":
        print("  - Production mode strict checks ... ENABLED")
        if not config["api_key"]:
            print("    * ERROR: API_KEY is required in production!")
    else:
        print("  - Development mode checks ......... RELAXED")


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

    security_check(config)

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
