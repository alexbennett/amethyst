#!/bin/bash

# Collect static
echo "Running collectstatic..."
python3 application/manage.py collectstatic --clear --no-input

# Start gunicorn
echo "Gunicorn Django websocket started!"
gunicorn core.wsgi \
    --chdir=application \
    --workers 1 \
    --timeout 120 \
    --bind=0.0.0.0:8000 \
    --log-level=debug
