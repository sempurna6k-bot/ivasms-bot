FROM mcr.microsoft.com/playwright/python:v1.48.0-focal

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Install browser
RUN python -m playwright install chromium --with-deps

CMD ["python", "app.py"]
