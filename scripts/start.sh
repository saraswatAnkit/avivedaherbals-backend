#!/bin/bash
cd /home/ubuntu/avivedaherbals-backend
docker compose down --remove-orphans
docker compose up -d --build
