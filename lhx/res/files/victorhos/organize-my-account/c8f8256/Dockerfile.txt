FROM python:3.9-rc-buster

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry

COPY poetry.lock pyproject.toml README.md /app/
RUN poetry export -f requirements.txt -o requirements.txt
RUN pip uninstall --yes poetry
RUN pip install --require-hashes -r requirements.txt

COPY . /app
