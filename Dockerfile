FROM python:3.8

LABEL maintainer="cwryu6252@naver.com"

COPY . /app/traffic_forecasting

RUN pip install -r /app/traffic_forecasting/traffic/requirements.txt
CMD ["python", "/app/traffic_forecasting/main.py"]
