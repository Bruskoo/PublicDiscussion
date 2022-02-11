# pull official base image
FROM python:3.9.6-alpine

# set work directory
COPY . /usr/src/PublicDiscussion
WORKDIR /usr/src/PublicDiscussion


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update\
    && pip install --upgrade pip\
    && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev gcc git\
    && pip install psycopg2-binary\
    && pip install -r requirements.txt


# run entrypoint.sh
COPY entrypoint.sh .
ENTRYPOINT ["sh", "/usr/src/PublicDiscussion/entrypoint.sh"]
