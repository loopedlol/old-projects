# Flask Form Validation

## Description
A Flask login form practice project with client-side username validation and a simple demo login check.

## Original Context
This was an older learning project.

## How to Run
Run from the project folder:

```sh
python3 -m pip install -r requirements.txt
python3 app.py
```

Open the local Flask URL shown in the terminal, usually `http://127.0.0.1:5000/`. The default demo login is username `demo` and password `password`, or set `DEMO_USERNAME` and `DEMO_PASSWORD`.

## Status
Partially works

## Cleanup Notes
- Renamed folder from `formvalidpro` to `flask-form-validation`.
- Moved screenshot and notes into `_excluded_review/`.
- Moved the original `app.py` with hardcoded credentials into `_excluded_review/security_review/`.
- Added a cleaned `app.py` that reads demo credentials from environment variables with harmless defaults.
- Fixed GET and failed-login responses.
- Fixed successful login to render `welcome.html`.
- Closed the missing Jinja block in `welcome.html`.
- Added `requirements.txt` and `.gitignore`.
