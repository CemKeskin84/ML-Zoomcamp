FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py","model.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["python", "predict.py"]