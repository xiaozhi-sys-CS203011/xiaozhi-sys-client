from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
APP_DIR = BASE_DIR / "app"
LOGS_DIR = BASE_DIR / "logs"
CONFIG_DIR = BASE_DIR
CONFIG_FILE = CONFIG_DIR / "config.json"
