#!/bin/bash

node gen-data.js

python3 gen-html.py

python3 gen-text.py
cat gen-text.py >> seeking.txt
python3 gen-text-html.py

