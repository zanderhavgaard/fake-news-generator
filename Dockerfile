FROM python:3.8.5-slim

RUN useradd --create-home --shell /bin/bash python

WORKDIR /home/python

COPY . /home/python

RUN pip install -r requirements.txt

USER python

EXPOSE 7890

ENTRYPOINT ["bash", "start.sh", "production"]
