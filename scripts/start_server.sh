while ! curl http://postgres:5432/ 2>&1 | grep '52'
do
  echo "Waiting for postgres..."
  sleep 1
done

/root/.local/bin/poetry run python manage.py migrate
/root/.local/bin/poetry run python manage.py runserver 0.0.0.0:8000

