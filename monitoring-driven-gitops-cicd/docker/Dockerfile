FROM python:3.10
WORKDIR /app
COPY app/ .
RUN pip install flask prometheus_client
ENV APP_VERSION=v1
CMD ["python", "app.py"]
