FROM python:3.12

WORKDIR /opt/project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFER 1
ENV PYTHONPATH .
ENV DJANGO_PROJECT_IN_DOCKER true

RUN set -xe \
    && apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install virtualenvwrapper poetry \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# No other than src/ and local/ directopries will be copied inside the container
COPY ["poetry.lock", "pyproject.toml", "./"]
RUN poetry install --no-root

COPY ["Makefile", "./"]
COPY src src
COPY local local

EXPOSE 8000

COPY ./bin/entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
