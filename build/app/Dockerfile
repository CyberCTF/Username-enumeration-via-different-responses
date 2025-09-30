FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Force rebuild by adding timestamp - Updated 2025-09-26 - Professional structure
RUN echo "Build timestamp: $(date)" > /app/build_info.txt

# Verify files are copied correctly
RUN cat app.py | grep -q "password1" || (echo "ERROR: password1 not found in app.py" && exit 1)
RUN cat templates/login.html | grep -q "Sign in" || (echo "ERROR: Updated login.html not found" && exit 1)
RUN cat app.py | grep -q "employees_directory" || (echo "ERROR: employees_directory route not found" && exit 1)
RUN cat app.py | grep -q "admin_password.*password1" || (echo "ERROR: admin_password not set to password1" && exit 1)
RUN cat templates/base.html | grep -q "Employee Directory" || (echo "ERROR: Employee Directory link not found in header" && exit 1)

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Run the application
CMD ["python", "app.py"]