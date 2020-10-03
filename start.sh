#!/bin/bash

mode=$1

port=7890
host="0.0.0.0"

export FLASK_APP=fake_news_generator.py

if [ "$mode" = "development" ] ; then
    export FLASK_ENV=development
    flask run \
        --reload \
        --port "$port" \
        --host "$host"
elif [ "$mode" = "production" ] ; then
    export FLASK_ENV=production
    flask run \
        --port "$port" \
        --host "$host"
else
    echo "You must provide an environment, either development or production"
fi
