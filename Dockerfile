FROM python:3.7

WORKDIR /Food_Ordering_service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5004

CMD ["python", "./server.py"]