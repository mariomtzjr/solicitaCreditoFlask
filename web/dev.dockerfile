FROM python:3.6-alpine

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

#Install extra libs for mysql
RUN apk add --update --upgrade --no-cache --virtual .build-deps\
    musl-dev \
    gcc \
    postgresql-dev \
    py-imaging \
    jpeg-dev \
    zlib-dev \
    py3-reportlab \
    glib \
    git \
    ca-certificates \
    nano \
    curl

# Add dev-requirements.txt file to container
ADD ./web/dev-requirements.txt /dev-requirements.txt
ADD ./web/dev.dockerfile /dev.dockerfile

# Update pip & install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /dev-requirements.txt

# Creation of the workdir
RUN mkdir /code

WORKDIR /code

ADD ./ /code/
