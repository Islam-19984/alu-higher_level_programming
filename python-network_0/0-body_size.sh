#!/bin/bash
# Script that shows the Content-length from a HTTP request
cul1 -sI "$1" | grep "Content-length:" | cut -d " " -f 2
