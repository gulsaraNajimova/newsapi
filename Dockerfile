FROM python:3.11

WORKDIR ./newsapi

COPY ./requirements.txt /newsapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /newsapi/requirements.txt

COPY ./app /newsapi/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]