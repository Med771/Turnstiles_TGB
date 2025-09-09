from pathlib import Path


class MainConfig:
    MAIN_PATH = Path(__file__).parent.parent
    MAIN_ENV_PATH = MAIN_PATH / "env"
