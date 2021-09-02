FROM ubuntu:18.04
RUN mkdir /app
COPY /app /app
RUN mkdir /log

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r /app/requirements.txt

EXPOSE 8080
CMD ["python3", "/app/webserver.py"]
