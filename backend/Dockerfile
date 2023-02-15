FROM python:3.10

WORKDIR /app 

COPY poetry.lock pyproject.toml /app/

RUN python3 -m pip install "poetry==1.3.1"
RUN poetry config virtualenvs.create true
RUN poetry config virtualenvs.in-project true
RUN poetry install

COPY . .

CMD ["poetry", "run", "uvicorn", "app.__main__:app", "--host", "0.0.0.0", "--port", "3000"]
