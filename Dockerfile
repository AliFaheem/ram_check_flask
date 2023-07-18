FROM python:3.10.9

WORKDIR /flask-docker

ADD . /Ram_Evaluation
EXPOSE 8080
EXPOSE 3306
COPY requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python", "./src/flask_code.py"]
