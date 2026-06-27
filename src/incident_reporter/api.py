import httpx
from incident_reporter.models import Incident, ApiConfig


class ApiClient:
    def __init__(self, config: ApiConfig) -> None:
        self.base_url = config.url

    def fetch_incidents(self) -> list[Incident]:
        response = httpx.get(self.base_url, timeout=10.0)
        response.raise_for_status()

        data = response.json()

        incidents: list[Incident] = []

        for item in data:
            incidents.append(
                Incident(
                    id=item["id"],
                    title=item["title"],
                    description=item["body"],
                )
            )

        return incidents