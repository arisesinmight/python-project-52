MANAGE := uv run python manage.py

shell:
	@$(MANAGE) shell_plus --ipython

run:
	@$(MANAGE) runserver
