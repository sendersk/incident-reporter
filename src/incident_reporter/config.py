from pathlib import Path
import yaml

from incident_reporter.models import AppConfig

CONFIG_PATH = Path("config/config.yaml")


def load_config() -> AppConfig:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return AppConfig.model_validate(data)