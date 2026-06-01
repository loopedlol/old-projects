# Flask SocketIO Form

## Description
A small Flask-SocketIO app that sends form messages to the server and displays the echoed message on the page.

## Original Context
This was an older learning project.

## How to Run
Run from the project folder:

```sh
python3 -m pip install -r requirements.txt
python3 app.py
```

Open the local URL shown in the terminal.

## Status
Partially works

## Cleanup Notes
- Renamed folder from `SocketsTest` to `flask-socketio-form`.
- Moved screenshot and notes into `_excluded_review/`.
- Moved the original `app.py` with a hardcoded secret placeholder into `_excluded_review/security_review/`.
- Added a cleaned `app.py` that reads `FLASK_SECRET_KEY` from the environment with a development fallback.
- Added `requirements.txt` and `.gitignore`.
