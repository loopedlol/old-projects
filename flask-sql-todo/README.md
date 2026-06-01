# Flask SQL Todo

## Description
A partially working Flask todo-list shell intended for SQL/database practice.

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
- Renamed folder from `sql` to `flask-sql-todo`.
- Moved `.vscode/`, screenshot, and notes into `_excluded_review/`.
- Changed the home route to render the existing `home.html` template with an empty list.
- Fixed the stylesheet path in `layout.html`.
- Added `requirements.txt` and `.gitignore`.
