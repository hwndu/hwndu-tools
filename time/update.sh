#!/bin/sh

cd ~/hwndu-tools/time
git pull
python generate_time.py
git add .
git commit -m "Update time"
git push

