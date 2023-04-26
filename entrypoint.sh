#!/bin/sh

"", "", "", "", "", "", "3000"]

uvicorn main:app --proxy-headers --host 0.0.0.0 --port $PORT --workers 12