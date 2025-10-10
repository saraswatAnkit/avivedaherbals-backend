#!/bin/bash
cd /home/ubuntu/avivedaherbals-backend
docker compose down --remove-orphans --volumes
docker compose up -d --build
