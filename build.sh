#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

if [ "${SEED_DEMO_DATA:-false}" = "true" ]; then
  python manage.py populate_demo_portal
fi
