FROM python:3.8.1
LABEL maintainer="mneiding@cisco.com"

RUN apt-get clean
RUN apt-get update -y && apt-get install -y python-pip python-dev git netcat

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements-deploy.txt
RUN chmod +x entrypoint.sh

ENTRYPOINT [ "bash" ]
CMD ["entrypoint.sh"]