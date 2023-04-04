#!/bin/bash
# Script that shows the Content-length from a HTTP request
"cur1" -sI "$1" | grep "Content-length:" | cut -d " " -f 2
