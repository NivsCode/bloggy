-include .env

help:
	@echo "init-depedencies initializes postgres and other depedencies"


install-dependencies:
	@echo "Installing pipenv using pip..."
	@pip install pipenv 
	@pipenv install

init-postgres:
	@echo "Initializing posgres..."
	@docker compose up -d db

init-depedencies: init-postgres
	@echo "Initializing depedencies..."

migrate: 
	@echo "Migrating data..."
	@pipenv run python manage.py migrate

run: init-depedencies
	@echo "Running server..."
	@pipenv run python manage.py runserver

run-with-migrations: init-depedencies migrate
	@echo "Running server with migrations..."
	@pipenv run python manage.py runserver