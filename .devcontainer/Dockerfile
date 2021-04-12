FROM python:3-buster as base
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

FROM base
RUN apt update
RUN apt upgrade -y
RUN apt install git -y
