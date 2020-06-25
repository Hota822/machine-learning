#!/bin/bash

if [ "$ENV" = 'development' ]; then
  apt-get update
  apt-get install -y procps
  apt-get clean
  rm -rf /var/lib/apt/lists/*
  echo '=================================='
  echo 'Development tools are installed'
  echo '=================================='
  echo
fi