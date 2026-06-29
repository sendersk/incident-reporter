from incident_reporter.api import ApiClient
from incident_reporter.config import load_config
from incident_reporter.reporter import HTMLReporter, MarkdownReporter
from incident_reporter.storage import Storage


def run_pipeline() -> None:
    """Execute the complete incident processing pipeline."""

    config = load_config()

    # Fetch incidents from REST API
    client = ApiClient(config.api.url)
    incidents = client.fetch_incidents()

    # Save incidents to JSON
    storage = Storage(config.storage.file)
    storage.save(incidents)

    # Generate reports
    markdown_reporter = MarkdownReporter(config.reports.markdown)
    markdown_reporter.generate(incidents)

    html_reporter = HTMLReporter(config.reports.html)
    html_reporter.generate(incidents)

    print("=== Incident Reporter ===")
    print(f"Fetched incidents : {len(incidents)}")
    print(f"JSON output       : {config.storage.file}")
    print(f"Markdown report   : {config.reports.markdown}")
    print(f"HTML report       : {config.reports.html}")
    print("[PIPELINE] Finished successfully")


def main() -> None:
    """Application entry point."""
    run_pipeline()


if __name__ == "__main__":
    main()