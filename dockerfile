# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install necessary system packages (including GTK libraries for WeasyPrint)
RUN apt-get update && apt-get install -y \
    libgdk-pixbuf-2.0-0 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    libfontconfig1 \
    libffi-dev \
    libcairo2 \
    && rm -rf /var/lib/apt/lists/*

# Install WeasyPrint and other Python dependencies
RUN pip install --no-cache-dir weasyprint streamlit

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Expose the port for Streamlit
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "pdf.py"]
