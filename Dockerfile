FROM python:3.8.2-slim-buster as production
ENV PYTHONUNBUFFERED=1
WORKDIR /agri_django
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt