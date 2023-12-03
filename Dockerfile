FROM python:3.10

WORKDIR /branch
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . ./
