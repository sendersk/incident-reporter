from .config import load_config

def main() -> None:
    config = load_config()

    print("=== Incident Reporter ===")
    print(f"API URL: {config.api.url}")
    print(f"Storage: {config.storage.file}")
    print(f"Markdown: {config.reports.markdown}")
    print(f"HTML: {config.reports.html}")


if __name__ == "__main__":
    main()