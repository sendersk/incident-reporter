from incident_reporter.models import Incident
from incident_reporter.reporter import MarkdownReporter


def test_markdown_report_generation(tmp_path):
    output_file = tmp_path / "report.md"

    reporter = MarkdownReporter(str(output_file))

    incidents = [
        Incident(id=1, title="Error A", description="Something broke"),
        Incident(id=2, title="Error B", description="Another issue"),
    ]

    reporter.generate(incidents)

    content = output_file.read_text(encoding="utf-8")

    assert "# Incident Report" in content
    assert "Error A" in content
    assert "Error B" in content