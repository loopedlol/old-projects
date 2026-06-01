# Flask Login Counter

## Description
A small Flask session practice app that logs in a username and tracks visit counts.

## Original Context
This was an older learning project.

## How to Run
Run from the project folder:

```sh
python3 -m pip install -r requirements.txt
python3 app.py
```

Open the local Flask URL shown in the terminal, usually `http://127.0.0.1:5000/`.

## Status
Partially works

## Cleanup Notes
- Renamed folder from `Idkprojectflask` to `flask-login-counter`.
- Moved screenshot and notes into `_excluded_review/`.
- Moved the original `app.py` with a hardcoded secret placeholder into `_excluded_review/security_review/`.
- Added a cleaned `app.py` that reads `FLASK_SECRET_KEY` from the environment with a development fallback.
- Fixed session visit initialization and consistent count rendering.
- Added `requirements.txt` and `.gitignore`.
