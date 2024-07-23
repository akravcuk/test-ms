#!/bin/bash

export FLASK_APP=app.py
export FLASK_DEBUG=1

# keep the following lines commented out to use the default user
# export USER_NAME="test"
# export USER_PASSWORD="test"

flask run --host=localhost --port=5000