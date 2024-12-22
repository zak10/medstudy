# ./Dockerfile
# pull official base image
FROM python:3.11-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1s

# install linux dependencies
# these may vary by project
# this list is relatively lightweight
# and it handles most of what I need
RUN apk update && apk upgrade && \
  apk add --no-cache gcc g++ musl-dev curl libffi-dev postgresql-dev zlib-dev jpeg-dev freetype-dev postgresql-client

# install poetry to manage python dependencies
RUN curl -sSL https://install.python-poetry.org | python3 -
# add poetry to path
ENV PATH="$PATH:/root/.local/bin/"

# install python dependencies
COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN poetry install

# copy project
COPY . .
# run at port 8000
EXPOSE 8000
CMD /app/scripts/start_server.sh
