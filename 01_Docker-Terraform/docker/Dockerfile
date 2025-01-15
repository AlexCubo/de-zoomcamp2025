FROM python:3.12.8

WORKDIR /app

COPY requirements.txt requirements.txt
COPY data data
COPY ingest_data.py ingest_data.py
#COPY pipeline.py pipeline.py

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "ingest_data.py" ]

#ENTRYPOINT [ "bash" ]
#ENTRYPOINT [ "python", "pipeline.py" ]