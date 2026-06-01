# Flask Session Login

## Description
A small Flask session-login practice app that stores a username in the session.

## Original Context
This was an older learning project.

## How to Run
Run from the project folder:

```sh
python3 -m pip install -r requirements.txt
python3 app.py
```

Open `http://localhost:5555/`.

## Status
Partially works

## Cleanup Notes
- Renamed folder from `hopefullast` to `flask-session-login`.
- Moved screenshot and notes into `_excluded_review/`.
- Moved the original `app.py` with a hardcoded secret and import issues into `_excluded_review/security_review/`.
- Added a cleaned `app.py` with correct imports, `FLASK_SECRET_KEY` support, and fixed port handling.
- Added `requirements.txt` and `.gitignore`.
