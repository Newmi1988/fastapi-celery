FROM python:3.8.6-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.1.4 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"


# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# install deps
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        curl \
        # deps for building python deps
        build-essential

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry export --without-hashes > requirements.txt \
    && poetry run pip install -r requirements.txt \
    && rm requirements.txt

COPY ./src ./src
RUN poetry install --no-dev

# `development` image is used during development / testing
# FROM python-base as development
# ENV FASTAPI_ENV=development
# WORKDIR $PYSETUP_PATH

# # copy in our built poetry + venv
# COPY --from=builder-base $POETRY_HOME $POETRY_HOME
# COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# # quicker install as runtime deps are already installed
# RUN poetry install

# WORKDIR /app

# EXPOSE 8000
# CMD ["celery", "--app" "api.celery.worker:app" "worker" "--loglevel=INFO"]

# `production` image used for runtime
FROM python-base as production
ENV ISPRODUCTION=1
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
COPY ./src /app/src
WORKDIR /app
CMD ["celery","--app","celeryworker.worker:app","worker"]

