import sys

from incident_reporter.logging import setup_logger
from incident_reporter.pipeline import run_pipeline
from incident_reporter.scheduler import IncidentScheduler


# initialize global logger
logger = setup_logger()


def main() -> None:
    """Application entry point."""

    logger.info("Starting Incident Reporter service...")

    if "--schedule" in sys.argv:
        scheduler = IncidentScheduler()
        scheduler.start()
    else:
        run_pipeline()


if __name__ == "__main__":
    main()