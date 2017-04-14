#!/bin/sh


# Make sure to create env.list before, use env.list.template as a template

docker run -p 8000:80 --env-file ./env.list -v $(pwd)/db.sqlite3:/code/db.sqlite3 hackcu/mercurysms:1.0.1