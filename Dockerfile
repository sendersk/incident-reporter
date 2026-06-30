FROM python:3.13-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# install uv
RUN pip install uv

# copy dependency files first (cache layer)
COPY pyproject.toml uv.lock ./

# install dependencies
RUN uv sync --frozen

# copy source code
COPY src ./src
COPY config ./config
COPY templates ./templates

# create runtime dirs
RUN mkdir -p data reports

CMD ["uv", "run", "python", "src/incident_reporter/main.py"]