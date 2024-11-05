# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install the necessary system packages (including GTK libraries)
RUN apt-get update && apt-get install -y \
    libgobject-2.0-0 \
    libpango-1.0-0 \
    libfontconfig1 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libcairo2 \
    libffi-dev \
    libxml2-dev \
    libjpeg62-turbo \
    build-essential \
    wget

# Install WeasyPrint and other Python dependencies
RUN pip install weasyprint streamlit

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Expose port 8501 to access the Streamlit app
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "pdf.py"]
