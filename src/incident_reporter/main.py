from incident_reporter.api import ApiClient
from incident_reporter.config import load_config


def main() -> None:
    config = load_config()

    client = ApiClient(config.api)
    incidents = client.fetch_incidents()

    print("=== Incident Reporter ===")
    print(f"Fetched incidents: {len(incidents)}")

    print("\nSample incident: ")
    print(incidents[0])


if __name__ == "__main__":
    main()