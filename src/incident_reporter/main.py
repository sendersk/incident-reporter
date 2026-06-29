import sys

from incident_reporter.pipeline import run_pipeline
from incident_reporter.scheduler import IncidentScheduler


def main() -> None:
    """Application entry point."""

    if "--schedule" in sys.argv:
        scheduler = IncidentScheduler()
        scheduler.start()
    else:
        run_pipeline()


if __name__ == "__main__":
    main()