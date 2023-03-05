FROM python:3.10

WORKDIR /app 

COPY poetry.lock pyproject.toml /app/

ARG APP_PORT
ENV APP_PORT=${APP_PORT}

RUN python3 -m pip install "poetry==1.3.1"
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

CMD poetry run uvicorn app.__main__:app --host 0.0.0.0 --port $APP_PORT

