from incident_reporter.models import Incident
from incident_reporter.reporter import HTMLReporter


def test_html_report(tmp_path):
    file_path = tmp_path / "report.html"

    reporter = HTMLReporter(str(file_path))

    incidents = [
        Incident(id=1, title="Test", description="Something broke")
    ]

    reporter.generate(incidents)

    content = file_path.read_text(encoding="utf-8")

    assert "<html" in content
    assert "Incident Report" in content
    assert "Test" in content