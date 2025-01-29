MANAGE := uv run python manage.py

shell:
	@$(MANAGE) shell_plus --ipython

run:
	@$(MANAGE) runserver

gunicorn:
	 uv run python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

migrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

trans:
	uv run django-admin makemessages -l ru_RU

comp:
	uv run django-admin compilemessages
test-coverage:
	coverage run manage.py test task_manager
	coverage report