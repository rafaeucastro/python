FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

WORKDIR /app/src

EXPOSE 8005

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8005" ]