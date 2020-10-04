#!/bin/bash

image_name="zanderhavgaard/fake-news-generator"
git_sha=$(git rev-parse --short HEAD)

echo "--> Building docker image ..."

docker build -f "Dockerfile" -t "$image_name:$git_sha" .
docker tag "$image_name:$git_sha" "$image_name:latest"

echo "--> Done building new docker image."
