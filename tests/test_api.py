from incident_reporter.api import ApiClient
from incident_reporter.models import AppConfig, ApiConfig


def test_api_client_fetches_data():
    config = ApiConfig(url="https://jsonplaceholder.typicode.com/posts")

    client = ApiClient(config)
    incidents = client.fetch_incidents()

    assert isinstance(incidents, list)
    assert len(incidents) > 0
    assert hasattr(incidents[0], "id")