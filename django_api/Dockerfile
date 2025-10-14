FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt 
WORKDIR /app/src

# EXPOSE 8008

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8008" ]