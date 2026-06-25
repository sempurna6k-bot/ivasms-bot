FROM mcr.microsoft.com/playwright/python:v1.48.0-focal

WORKDIR /app

# Install dependencies dulu
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Install hanya chromium (lebih ringan)
RUN python -m playwright install chromium --with-deps

ENV PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=0
ENV PYTHONUNBUFFERED=1
ENV NODE_ENV=production

# Kurangi memory usage
ENV PLAYWRIGHT_BROWSER_ARGS="--no-sandbox,--disable-setuid-sandbox,--disable-dev-shm-usage"

CMD ["python", "app.py"]
