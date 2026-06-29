from incident_reporter.api import ApiClient
from incident_reporter.config import load_config
from incident_reporter.reporter import MarkdownReporter, HTMLReporter
from incident_reporter.storage import Storage


def main() -> None:
    config = load_config()

    client = ApiClient(config.api)
    incidents = client.fetch_incidents()

    storage = Storage(config.storage.file)
    storage.save(incidents)

    md_reporter = MarkdownReporter(config.reports.markdown)
    md_reporter.generate(incidents)

    html_reporter = HTMLReporter(config.reports.html)
    html_reporter.generate(incidents)

    print("=== Incident Reporter ===")
    print(f"Fetched incidents: {len(incidents)}")
    print(f"Saved JSON: {config.storage.file}")
    print(f"Markdown: {config.reports.markdown}")
    print(f"HTML: {config.reports.html}")


if __name__ == "__main__":
    main()