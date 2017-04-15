#!/bin/sh

# Update with new tags
docker pull hackcu/mercurysms:1.0.3
docker stop mercurysms
docker rm mercurysms

# Make sure to create env.list before, use env.list.template as a template
docker run -d -p 8000:80 --name mercurysms --env-file ./env.list -v $(pwd)/database:/code/db hackcu/mercurysms:1.0.3