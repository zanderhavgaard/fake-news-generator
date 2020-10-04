#!/bin/bash

image_name="zanderhavgaard/fake-news-generator"
git_sha=$(git rev-parse --short HEAD)

echo "--> Pushing new docker image ..."

docker push "$image_name:$git_sha"
docker push "$image_name:latest"

echo "--> Done pushing new docker image."
