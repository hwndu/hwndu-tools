#!/bin/sh

mkdir complete
while true; do python stream.py; mv *.flv complete; done
