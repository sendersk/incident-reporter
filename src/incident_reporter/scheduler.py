from apscheduler.schedulers.blocking import BlockingScheduler

from incident_reporter.pipeline import run_pipeline


class IncidentScheduler:
    def __init__(self) -> None:
        self.scheduler = BlockingScheduler()

    def start(self) -> None:
        self.scheduler.add_job(
            run_pipeline,
            trigger="interval",
            minutes=1,
            id="incident_report_job",
            replace_existing=True,
        )

        print("Scheduler started. Generating reports every minute...")

        try:
            self.scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            print("Scheduler stopped.")