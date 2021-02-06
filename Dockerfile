FROM python:3.6
WORKDIR /OJ-Counter/

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
