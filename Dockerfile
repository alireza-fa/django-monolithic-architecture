FROM python

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
