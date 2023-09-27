FROM python:3.10.2

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m venv venv
CMD ["venv/Scripts/activate"]
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]