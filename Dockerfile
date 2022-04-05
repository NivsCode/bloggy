FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /bloggy
COPY . /bloggy/
# COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install


# CMD pipenv run python manage.py runserver