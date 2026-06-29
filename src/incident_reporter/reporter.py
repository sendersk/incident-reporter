from datetime import datetime, UTC
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from incident_reporter.models import Incident


class MarkdownReporter:
    def __init__(self, output_path: str) -> None:
        self.output_path = Path(output_path)

    def generate(self, incidents: list[Incident]) -> None:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        content = self._build_report(incidents)

        self.output_path.write_text(content, encoding="utf-8")

    def _build_report(self, incidents: list[Incident]) -> str:
        lines: list[str] = []

        lines.append("# Incident Report\n")
        lines.append(f"Generated: {datetime.now(UTC).isoformat()} UTC\n")
        lines.append(f"Total incidents: {len(incidents)}\n")
        lines.append("---\n")

        for inc in incidents[:10]:
            lines.append(f"## Incident #{inc.id}\n")
            lines.append(f"**Title:** {inc.title}\n")
            lines.append(f"**Description:** {inc.description}\n")
            lines.append("---\n")

        return "\n".join(lines)


class HTMLReporter:
    def __init__(self, output_path: str) -> None:
        self.output_path = Path(output_path)

        self.env = Environment(loader=FileSystemLoader("templates"))

    def generate(self, incidents: list[Incident]) -> None:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        template = self.env.get_template("report.html.j2")

        html = template.render(
            incidents=incidents,
            generated_at=datetime.utcnow().isoformat()
        )

        self.output_path.write_text(html, encoding="utf-8")