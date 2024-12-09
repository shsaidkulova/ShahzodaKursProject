FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r req.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
