web: gunicorn --pythonpath nwo nwo.wsgi
release: python manage.py migrate
worker: celery -A nwo.celery_worker worker --concurrency=2 --loglevel=INFO
