FROM python:latest
RUN mkdir /be2
RUN apt update
RUN apt install nano
RUN pip install poetry
WORKDIR /be2
COPY poetry.lock /be2/
COPY pyproject.toml /be2/
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . /be2/