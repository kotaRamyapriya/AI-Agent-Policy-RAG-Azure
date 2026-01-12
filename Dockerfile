# 1. Use Python 3.10 as the base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your project files into the container
COPY . .

# 4. Install the libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the port the app runs on
EXPOSE 8000

# 6. Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]