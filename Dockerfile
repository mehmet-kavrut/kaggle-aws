# Use official Airflow image as base
FROM apache/airflow:3.0.6

USER root
# Install system dependencies if needed
RUN apt-get update && apt-get install -y build-essential curl

# Switch back to airflow user
USER airflow

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy DAGs and plugins into the image
COPY dags/ /opt/airflow/dags/
COPY plugins/ /opt/airflow/plugins/


