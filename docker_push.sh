#!/bin/bash
docker build . -t andrew-houghton/moon
echo "$GIT_TOKEN" | docker login docker.pkg.github.com -u "$GIT_USERNAME" --password-stdin
docker push andrew-houghton/moon
