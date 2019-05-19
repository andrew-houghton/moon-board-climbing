#!/bin/bash
docker build . -t andrew-houghton/moon
echo "$GIT_TOKEN" | docker login -u "$GIT_USERNAME" --password-stdin
docker push andrew-houghton/moon
