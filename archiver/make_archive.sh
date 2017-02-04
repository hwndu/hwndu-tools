#!/bin/bash

cd ~/hwndu-tools/archiver/
git pull
mkdir vids
mkdir thumbs

WORK="$(python archive.py)"
while read -r line; do
    FS=" "; declare -a Array=($line) 
    CVID="./vids/${Array[0]}.mp4"
    CTHU="./thumbs/${Array[0]}.jpg"
    NVID="gs://hwndu-video-backups/video/${Array[0]}.mp4"
    NTHU="gs://hwndu-video-backups/thumbnail/${Array[0]}.jpg"
    wget "${Array[1]}" -O "${CVID}"
    wget "${Array[2]}" -O "${CTHU}"
    gsutil cp "${CVID}" "${NVID}"
    gsutil cp "${CTHU}" "${NTHU}"
    gsutil acl ch -u AllUsers:R "${NVID}"
    gsutil acl ch -u AllUsers:R "${NTHU}"
    rm "${CVID}"
    rm "${CTHU}"
done <<< "$WORK"

rmdir vids
rmdir thumbs

./update_index.sh

git add .
git commit -m "Update archive"
git push

