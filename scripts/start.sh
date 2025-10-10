#!/bin/bash
cd /home/ubuntu/avivedaherbals-backend
docker compose down
docker compose up -d --build
