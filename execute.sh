#!/bin/bash
cd ./postgres_source
docker-compose up -d
python main.py
cd ../api_source
python main.py
cd ..