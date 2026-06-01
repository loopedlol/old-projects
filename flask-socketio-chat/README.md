# Flask SocketIO Chat

## Description
A small Flask-SocketIO message form that sends a message and displays the echoed response.

## Original Context
This was an older learning project.

## How to Run
Run from the project folder:

```sh
python3 -m pip install -r requirements.txt
python3 app.py
```

Open `http://localhost:5000/`.

## Status
Partially works

## Cleanup Notes
- Renamed folder from `loool` to `flask-socketio-chat`.
- Moved virtual environment, screenshot, and notes into `_excluded_review/`.
- Moved the original `app.py` with a hardcoded secret placeholder into `_excluded_review/security_review/`.
- Added a cleaned `app.py` that reads `FLASK_SECRET_KEY` from the environment with a development fallback.
- Fixed the form submit selector and message value lookup in `static/index.js`.
- Added `requirements.txt` and `.gitignore`.
