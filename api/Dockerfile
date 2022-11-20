FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY ./models /code/models
COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--reload", "--port", ${PORT}]
