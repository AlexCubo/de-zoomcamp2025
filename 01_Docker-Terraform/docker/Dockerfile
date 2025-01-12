FROM python:3.12

WORKDIR app/

COPY requirements.txt app/requirements.txt
COPY data app/data
COPY pipeline.py app/pipeline.py

RUN pip install -r app/requirements.txt

ENTRYPOINT [ "bash" ]