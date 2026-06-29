from apscheduler.schedulers.blocking import BlockingScheduler
from incident_reporter.main import run_pipeline


class IncidentScheduler:
    def __init__(self) -> None:
        self.scheduler = BlockingScheduler()

    def start(self) -> None:
        self.scheduler.add_job(run_pipeline, "interval", seconds=60)

        print("[SCHEDULER] Started - running every 60 seconds")

        self.scheduler.start()