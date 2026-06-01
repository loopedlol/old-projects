# Flask SocketIO Fork Practice

## Description
An archived Git/fork practice folder containing a small Flask-SocketIO message example.

## Original Context
This was an older learning project.

## How to Run
Archived. The nested Flask-SocketIO example can be run from `Flask-Sockets`:

```sh
python3 -m pip install -r requirements.txt
python3 app.py
```

## Status
Archived

## Cleanup Notes
- Renamed folder from `gitForkPractice` to `flask-socketio-fork-practice`.
- Moved top-level and nested `.git/` folders into `_excluded_review/`.
- Moved the original `Flask-Sockets/app.py` with a hardcoded secret placeholder into `_excluded_review/security_review/`.
- Moved `SecretPython.py` into `_excluded_review/security_review/` for review because of its filename.
- Added a cleaned `Flask-Sockets/app.py` that reads `FLASK_SECRET_KEY` from the environment with a development fallback.
- Added this README.
