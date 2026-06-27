from incident_reporter.models import Incident
from incident_reporter.storage import Storage


def test_storage_save_and_load(tmp_path):
    file_path = tmp_path / "incidents.json"

    storage = Storage(str(file_path))

    incidents = [
        Incident(id=1, title="t1", description="d1"),
        Incident(id=2, title="t2", description="d2"),
    ]

    storage.save(incidents)
    loaded = storage.load()

    assert len(loaded) == 2
    assert loaded[0]["id"] == 1