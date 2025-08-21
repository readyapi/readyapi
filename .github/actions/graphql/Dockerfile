FROM python:3.8

RUN pip install --no-cache --upgrade pip setuptools wheel

EXPOSE 7779/tcp
WORKDIR /app
CMD [ "python", "app.py" ]

COPY . /app

RUN pip install --no-cache -r requirements.txt
