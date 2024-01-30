FROM python

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install --upgrade pip

COPY requirements.txt /code/
COPY requirements/ /code/requirements

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
