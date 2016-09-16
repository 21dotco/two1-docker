#!/bin/sh

python3 utils/login.py && sleep 2 && python3 utils/update_manifest.py && sleep 2 && python3 server.py
