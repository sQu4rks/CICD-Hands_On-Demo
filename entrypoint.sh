#!/bin/bash
gunicorn --bind 0.0.0.0:8010 --timeout 500 --log-level=DEBUG --workers 4 app:app