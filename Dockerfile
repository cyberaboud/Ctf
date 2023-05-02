FROM python:3.7

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod 555 -R src

CMD ["gunicorn", "src.app:app", "-b", "0.0.0.0"]