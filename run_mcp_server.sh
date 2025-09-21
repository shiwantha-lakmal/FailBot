#!/bin/bash
cd /Users/shiwantha.lakmal/Personal/FailBot
source .venv/bin/activate
export PYTHONPATH=/Users/shiwantha.lakmal/Personal/FailBot/src
exec python3 src/mcpserver/service.py
