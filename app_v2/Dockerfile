FROM python:3.9-slim

RUN apt-get update && apt-get install -y build-essential python3-dev libpq-dev

WORKDIR /app

COPY . /app

RUN pip install --verbose -r requirements.txt

ENV APP_ENV=development

CMD ["python", "database_ingestion_runner.py"]
