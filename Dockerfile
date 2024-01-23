FROM python:3.9-slim

WORKDIR /app

EXPOSE 8501

COPY ./requirements.txt /app

RUN pip3 install -r /app/requirements.txt

COPY . /app

ENTRYPOINT ["streamlit", "run", "/app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]