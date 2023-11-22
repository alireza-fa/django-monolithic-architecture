FROM python

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000
