from incident_reporter.api import ApiClient
from incident_reporter.config import load_config
from incident_reporter.storage import Storage


def main() -> None:
    config = load_config()

    client = ApiClient(config.api)
    incidents = client.fetch_incidents()

    storage = Storage(config.storage.file)
    storage.save(incidents)

    print("=== Incident Reporter ===")
    print(f"Fetched incidents: {len(incidents)}")
    print(f"Saved to: {config.storage.file}")


if __name__ == "__main__":
    main()