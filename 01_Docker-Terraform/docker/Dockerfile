FROM python:3.12.8

WORKDIR /app

COPY requirements.txt requirements.txt
COPY data data
COPY pipeline.py pipeline.py

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "pipeline.py" ]

#NTRYPOINT [ "bash" ]