
#!/bin/bash

# Install dependencies
pip3.9 install -r requirements.txt

# Build static files (if applicable)
python manage.py collectstatic --noinput

# Run database migrations (if applicable)
python manage.py migrate

# Build any additional files or perform other build tasks here

# Start the Django server
python manage.py runserver 0.0.0.0:$PORT