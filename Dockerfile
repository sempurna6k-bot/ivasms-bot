FROM mcr.microsoft.com/playwright/python:v1.45.0-jammy  # versi lebih lama tapi lebih ringan

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Install browser dengan minimal deps
RUN python -m playwright install chromium --with-deps

ENV PYTHONUNBUFFERED=1
ENV PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=0

CMD ["python", "app.py"]
