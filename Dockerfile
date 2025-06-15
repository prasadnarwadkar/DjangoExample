FROM python:3.13-slim

WORKDIR /usr/src/app

# Install dependencies in a single step to reduce layers
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Remove unnecessary apt-get installs and updates
# If vim is required, consider using a lightweight alternative or installing it only in a separate build stage
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
