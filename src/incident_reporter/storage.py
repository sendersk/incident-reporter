import json
from pathlib import Path

from incident_reporter.models import Incident


class Storage:
    def __init__(self, file_path: str) -> None:
        self.file_path = Path(file_path)

    def save(self, incidents: list[Incident]) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        data = [Incident.model_dump() for incident in incidents]

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    def load(self) -> list[dict]:
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            return json.load(file)