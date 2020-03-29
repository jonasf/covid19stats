FROM python:3.8.2-slim-buster

WORKDIR /app

COPY src/*.py ./
COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./get-covid19-stats.py" ]