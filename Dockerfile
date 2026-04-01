# syntax=docker/dockerfile:1
FROM python:3.11
RUN groupadd -r appuser && useradd -l -g appuser -r appuser
WORKDIR /app

RUN --mount=type=bind,src=requirements.txt,dst=requirements.txt pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser . .
USER appuser

ENTRYPOINT ["python", "main.py"]
