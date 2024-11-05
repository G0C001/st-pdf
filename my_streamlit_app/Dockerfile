
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \       
    libpango-1.0-0 \
    libfontconfig1 \
    libpangoft2-1.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY pdf.py .

EXPOSE 8501

CMD ["streamlit", "run", "pdf.py", "--server.port=8501", "--server.address=0.0.0.0"]
