FROM python:3-buster
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
