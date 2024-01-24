FROM python:3.11.6

WORKDIR /srv/www/static-tex

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY static_tex.py ./static_tex.py

CMD python static_tex.py build && python static_tex.py runserver

