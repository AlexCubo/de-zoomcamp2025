FROM python:3.12

WORKDIR app/

COPY requirements.txt app/requirements.txt
COPY data app/data

RUN pip install -r /app/requirements.txt

ENTRYPOINT [ "bash" ]