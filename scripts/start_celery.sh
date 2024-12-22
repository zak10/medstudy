#!/bin/bash
while ! curl http://postgres:5432/ 2>&1 | grep '52'
do
  echo "Waiting for postgres..."
  sleep 1
done

/root/.local/bin/poetry run watchfiles "celery -A nwo.celery_worker worker --concurrency=2 --loglevel=INFO"

