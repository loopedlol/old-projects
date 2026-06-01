# Cleanup Plan

## Batch 1 - 2026-05-31

## APIProject
- Suggested name: `age-api-project`
- Category: Keep but Rename
- Language/framework: HTML, CSS, JavaScript; browser fetch API using agify.io
- Main entry point: `index.html`
- Current status: Appears runnable by opening `index.html` in a browser, assuming internet access for the external API.
- Problems found: No README or `.gitignore`. No local dependency file needed. User input is inserted into the API URL without `encodeURIComponent`, so names with spaces or special characters may break requests.
- Functionality fixes needed: Encode the submitted name before building the API URL. Optionally add minimal fetch error handling so API/network failures do not silently fail.
- Files to exclude or move to `_excluded_review/`: None found.
- README needed: yes
- Recommendation: Keep as a small API/fetch learning project, rename to `age-api-project`, add simple run instructions.

## C# test
- Suggested name: `csharp-log-priority-practice`
- Category: Keep but Rename
- Language/framework: C# console app, .NET SDK project
- Main entry point: `ConsoleApp1/Program.cs`
- Current status: Not verified by build because `dotnet` is not installed in this environment. Source inspection suggests it likely does not compile because `Queue.cs` and `Stack.cs` both define `public class Queue<T>`.
- Problems found: Duplicate `Queue<T>` class definition in `Queue.cs` and `Stack.cs`. `Queue<T>.Pop()` removes the first item and then returns the new first item, not the removed item. Contains generated build output folders. Folder and solution names are generic.
- Functionality fixes needed: Fix or remove the duplicate class definition, likely by making `Stack.cs` actually define a stack or excluding it if accidental. Fix `Pop()` to return the removed item. Confirm `dotnet build` after changes.
- Files to exclude or move to `_excluded_review/`: `ConsoleApp1/bin/`, `ConsoleApp1/obj/`; consider moving `.vscode/` if it only contains personal editor settings.
- README needed: yes
- Recommendation: Keep as a C# data-structure/logging practice project after minimal compile/runtime fixes.

## C#practice
- Suggested name: `csharp-area-practice`
- Category: Keep but Rename
- Language/framework: C# console app, .NET SDK project
- Main entry point: `idktoName/Program.cs`
- Current status: Not verified by build because `dotnet` is not installed in this environment. Source inspection suggests it may fail as an executable because there is no `Main` method or top-level runnable code beyond comments and a `Program` class used like a rectangle object.
- Problems found: Generic folder/project name. `using System.ComponentModel;` appears unused. Contains generated build output folders. No README or `.gitignore`.
- Functionality fixes needed: Add a minimal `Main` method or top-level code that instantiates the class and prints a result, preserving the learning exercise. Optionally rename the class to something clearer only if needed for functionality/readability.
- Files to exclude or move to `_excluded_review/`: `idktoName/bin/`, `idktoName/obj/`; consider moving `.vscode/` if it only contains personal editor settings.
- README needed: yes
- Recommendation: Keep after adding a tiny runnable console entry point and excluding generated outputs.

## Calcth
- Suggested name: `flask-math-calculator`
- Category: Keep but Rename
- Language/framework: Python Flask app with HTML/CSS/JavaScript
- Main entry point: `app.py`
- Current status: Appears partly runnable with Flask installed, but several UI actions are unfinished or broken.
- Problems found: Bundled `.venv/` dependency environment should not go to GitHub. No `requirements.txt`, README, or project `.gitignore`. `static/script.js` does not return response text before writing results. `fibonacci()` and `average()` JavaScript functions are empty. `/average/<int:n>` route returns nothing. `next steps.txt` is project notes rather than runtime code. Screenshot file may be reference material rather than source.
- Functionality fixes needed: Add `requirements.txt` with Flask. Fix the factorial fetch chain to read `response.text()`. Implement the existing fibonacci button behavior. Either implement or disable/fix the average route and button so it does not error. Verify app starts with `python3 app.py`.
- Files to exclude or move to `_excluded_review/`: `.venv/`; possibly `Screenshot 2024-09-15 114524.png` and `next steps.txt` if they are not part of the project to publish.
- README needed: yes
- Recommendation: Keep as a Flask math learning app after small route/client fixes and dependency cleanup.

## FlaskStarterKit
- Suggested name: `flask-starter-kit`
- Category: Exclude / Template
- Language/framework: Python Flask starter/template with HTML/CSS/JavaScript
- Main entry point: `app.py`
- Current status: Appears runnable with Flask installed, but it is mostly boilerplate starter content.
- Problems found: Looks like copied starter/template structure rather than a distinct project. No `requirements.txt`, README, or `.gitignore`. `static/script.js` is empty. `next steps.txt` and screenshot may be notes/reference material, not source.
- Functionality fixes needed: If kept, add `requirements.txt` and minimal run instructions. No functional app-specific fix identified beyond dependency/run documentation.
- Files to exclude or move to `_excluded_review/`: Consider moving the whole folder to `_excluded_review/templates/` as copied starter boilerplate; otherwise consider excluding `Screenshot 2024-09-15 114524.png` and `next steps.txt`.
- README needed: yes, if kept
- Recommendation: Exclude as template/boilerplate unless you want to preserve it specifically as a Flask starter reference.

## Batch 2 - 2026-05-31

## Forum
- Suggested name: `flask-forum`
- Category: Keep but Rename
- Language/framework: Python Flask app with HTML/CSS/JavaScript
- Main entry point: `app.py`
- Current status: Partially runnable with Flask installed. The home and general pages exist, but some routes point to missing templates and the nav links include at least one route that does not exist.
- Problems found: No README, `.gitignore`, or `requirements.txt`. Routes `/books`, `/tv`, and `/about` render templates that are not present. The nav links to `/games`, but no `/games` route exists. `general.html` and `post.html` wrap Jinja `{% extends %}` inside full HTML, which may render oddly but is not necessarily a run blocker. `static/script.js` is empty. `Screenshot 2024-09-15 114524.png` and `next steps.txt` look like reference/notes files rather than source.
- Functionality fixes needed: Add missing templates or remove/adjust broken routes and nav links, preserving the simple forum/blog idea. Add `requirements.txt` with Flask. Verify `python3 app.py` starts and visible links do not 404.
- Files to exclude or move to `_excluded_review/`: Consider moving `Screenshot 2024-09-15 114524.png` and `next steps.txt`; move any generated caches if found later.
- README needed: yes
- Recommendation: Keep as a Flask forum/blog learning project after minimal route/template cleanup.

## Idkprojectflask
- Suggested name: `flask-login-counter`
- Category: Keep but Rename
- Language/framework: Python Flask app with sessions and HTML/CSS/JavaScript
- Main entry point: `app.py`
- Current status: Does not appear runnable as-is. The `/` route checks `session["visits"]` in the else branch before it exists, which should raise a `KeyError` for a new visitor.
- Problems found: Hardcoded Flask secret key placeholder in `app.py`; should not be published as-is. No README, `.gitignore`, or `requirements.txt`. Session visit counter is initialized incorrectly. `/login` renders `welcome.html` without `count`, while `welcome.html` expects `count`. `make_response` import appears unused. `static/script.js` is empty. `Screenshot 2024-09-15 114524.png` and `next steps.txt` look like reference/notes files rather than source.
- Functionality fixes needed: Replace the hardcoded secret with an environment variable plus a harmless development fallback, or move the original `app.py` to `_excluded_review/security_review/` and create a cleaned copy. Initialize `session["visits"]` before reading it. Pass `count` consistently when rendering `welcome.html`. Add `requirements.txt` with Flask.
- Files to exclude or move to `_excluded_review/`: Move the original file containing the hardcoded secret placeholder to `_excluded_review/security_review/` if preserving the exact original is required; consider moving `Screenshot 2024-09-15 114524.png` and `next steps.txt`.
- README needed: yes
- Recommendation: Keep as a small Flask session/login learning project after fixing the session crash and removing the hardcoded secret from the publishable code.

## JokeGame
- Suggested name: `joke-api-game`
- Category: Keep but Rename
- Language/framework: HTML, CSS, JavaScript; browser fetch API using official-joke-api.appspot.com
- Main entry point: `index.html`
- Current status: Appears runnable by opening `index.html` in a browser, assuming internet access and a valid joke type. It can break if the API returns an empty response or if the punchline button is clicked before a joke loads.
- Problems found: No README or `.gitignore`. Joke type is inserted into the URL without `encodeURIComponent`. No error handling for unknown joke types, network failures, or clicking punchline before a joke is loaded.
- Functionality fixes needed: Encode the joke type before building the API URL. Add minimal checks/error messages for empty API responses and punchline-before-joke, without changing the UI concept.
- Files to exclude or move to `_excluded_review/`: None found.
- README needed: yes
- Recommendation: Keep as a small browser API learning project.

## Mandelbrot
- Suggested name: `mandelbrot-viewer`
- Category: Keep but Rename
- Language/framework: Python using Pillow and Matplotlib
- Main entry point: `mandelbrotV3.py`
- Current status: Source files pass syntax-only compile checks. Runtime was not verified because Pillow and Matplotlib are not installed in this environment. The main script should generate and display a Mandelbrot image when dependencies are available.
- Problems found: Bundled `env/` virtual environment and `__pycache__/` should not go to GitHub. No README, `.gitignore`, or `requirements.txt`. `garbage/` contains older experiments/scratch scripts and should be reviewed rather than published as primary source. `mandelbrotV3.py` uses `image.show()`, which may require a local image viewer.
- Functionality fixes needed: Add `requirements.txt` with Pillow and Matplotlib. Add run instructions. Optionally rename or document `mandelbrotV3.py` as the main entry point; only change code if runtime testing reveals a dependency/API issue.
- Files to exclude or move to `_excluded_review/`: `env/`, `__pycache__/`, and likely `garbage/`.
- README needed: yes
- Recommendation: Keep as a Python fractal learning project after removing generated environment/cache folders and moving scratch experiments aside.

## PygameGame
- Suggested name: `pygame-dungeon-game`
- Category: Keep but Rename
- Language/framework: Python Pygame
- Main entry point: `main.py`
- Current status: Source files pass syntax-only compile checks. Runtime was not verified because Pygame is not installed in this environment. The code appears to open a fullscreen-sized generated level using image assets.
- Problems found: Bundled `.venv/` and `__pycache__/` should not go to GitHub. No README, `.gitignore`, or `requirements.txt`. Uses relative image paths, so it likely must be run from the project folder. `process_events()` assigns `running = False` without declaring it global, so closing the window may not stop the main loop correctly. Project name is generic.
- Functionality fixes needed: Add `requirements.txt` with pygame. Add `global running` inside `process_events()` or otherwise minimally fix quit handling. Document that it should be run from the project directory with `python3 main.py`. Verify once pygame is installed.
- Files to exclude or move to `_excluded_review/`: `.venv/`, `__pycache__/`.
- README needed: yes
- Recommendation: Keep as a Pygame learning project with its asset folder intact, after removing generated environment/cache folders and fixing quit handling.

## Batch 3 - 2026-05-31

## SocketsTest
- Suggested name: `flask-socketio-form`
- Category: Keep but Rename
- Language/framework: Python Flask with Flask-SocketIO, HTML/CSS/JavaScript
- Main entry point: `app.py`
- Current status: Source passes syntax-only compile checks. Runtime was not verified because Flask and Flask-SocketIO are not installed in this environment. The app appears intended to echo form submissions over a Socket.IO namespace.
- Problems found: Hardcoded Flask `SECRET_KEY` placeholder in `app.py`; should not be published as-is. No README, `.gitignore`, or `requirements.txt`. `Screenshot 2024-09-15 114524.png` and `next steps.txt` look like reference/notes files rather than source.
- Functionality fixes needed: Replace the hardcoded secret with an environment variable plus harmless development fallback, or move the original `app.py` to `_excluded_review/security_review/` and create a cleaned copy. Add `requirements.txt` with Flask and Flask-SocketIO. Verify `python3 app.py` starts after dependencies are installed.
- Files to exclude or move to `_excluded_review/`: Move the original file containing the hardcoded secret placeholder to `_excluded_review/security_review/` if preserving the exact original is required; consider moving `Screenshot 2024-09-15 114524.png` and `next steps.txt`.
- README needed: yes
- Recommendation: Keep as a small Flask-SocketIO learning project after secret cleanup and dependency/run documentation.

## Temp
- Suggested name: `flask-door-game`
- Category: Keep but Rename
- Language/framework: Python Flask with HTML/CSS/JavaScript
- Main entry point: `app.py`
- Current status: Source passes syntax-only compile checks. Runtime was not verified because Flask is not installed in this environment. The app appears runnable as a simple choose-a-door game once Flask is installed.
- Problems found: Folder name is temporary/generic. No README, `.gitignore`, or `requirements.txt`. `Screenshot 2024-09-15 114524.png` and `next steps.txt` look like reference/notes files rather than source. Uses externally hosted image URLs, so result images depend on internet access and those links staying valid.
- Functionality fixes needed: Add `requirements.txt` with Flask and run instructions. No code fix identified from source inspection unless runtime testing reveals a Flask/template issue.
- Files to exclude or move to `_excluded_review/`: Consider moving `Screenshot 2024-09-15 114524.png` and `next steps.txt`.
- README needed: yes
- Recommendation: Keep as a small Flask door-prize learning project.

## backendsec
- Suggested name: `flask-auth-db-experiment`
- Category: Archive
- Language/framework: Python Flask with attempted SQLAlchemy usage
- Main entry point: `app.py`
- Current status: Source passes syntax-only compile checks, but appears not runnable as-is. `app.py` renders missing `index.html`, has no `/login` or `/signup` routes despite templates, uses `sqlalchemy(app)` instead of a Flask SQLAlchemy app object, and has a typo `db.Interger`.
- Problems found: Hardcoded Flask secret in `app.py`; should not be published as-is. No README, `.gitignore`, or `requirements.txt`. Database URI string appears malformed. The database model and routes are incomplete. `next steps.txt` looks like notes rather than source.
- Functionality fixes needed: If kept as runnable instead of archived, move the original `app.py` to `_excluded_review/security_review/`, create a cleaned app with an environment-based secret, add proper Flask-SQLAlchemy setup, fix `Integer`, add missing routes/templates wiring, and add dependencies. This may be more work than a minimal cleanup, so archive is recommended.
- Files to exclude or move to `_excluded_review/`: Move original `app.py` to `_excluded_review/security_review/`; consider moving `next steps.txt`.
- README needed: yes
- Recommendation: Archive as an incomplete backend auth/database experiment, with security-sensitive original code kept out of the publishable project.

## clickerGame
- Suggested name: `flask-socketio-clicker`
- Category: Keep but Rename
- Language/framework: Python Flask with Flask-SocketIO, HTML/CSS/JavaScript
- Main entry point: `app.py`
- Current status: Source passes syntax-only compile checks. Runtime was not verified because Flask and Flask-SocketIO are not installed in this environment. The current server echoes Socket.IO messages, while the page has the beginnings of a clicker game UI.
- Problems found: No README, `.gitignore`, or `requirements.txt`. The start button has no visible text. `static/app.js` connects and sends a test message but does not implement visible clicker behavior yet. App may need to be run from the project folder so static/template paths work normally.
- Functionality fixes needed: Add `requirements.txt` with Flask and Flask-SocketIO. Add minimal visible button text and/or minimal existing click action only if needed to demonstrate the current clicker idea; avoid adding major gameplay. Verify `python3 app.py` starts after dependencies are installed.
- Files to exclude or move to `_excluded_review/`: None found.
- README needed: yes
- Recommendation: Keep as a small Flask-SocketIO/clicker learning project, preserving the early prototype feel.

## formvalidpro
- Suggested name: `flask-form-validation`
- Category: Keep but Rename
- Language/framework: Python Flask with HTML/CSS/JavaScript form validation
- Main entry point: `app.py`
- Current status: Source passes syntax-only compile checks, but does not appear runnable as-is for a GET request because the `/` route can finish without returning a response. It also contains hardcoded login credentials.
- Problems found: Hardcoded username/password in `app.py`; should not be published as-is. No README, `.gitignore`, or `requirements.txt`. Successful login renders `index.html` instead of `welcome.html`, so the success page is not used. Failed login sets `message` but does not return a template. `welcome.html` has an unclosed Jinja `{% if message %}` block. `Screenshot 2024-09-15 114524.png` and `next steps.txt` look like reference/notes files rather than source.
- Functionality fixes needed: Move the original `app.py` with hardcoded credentials to `_excluded_review/security_review/` and create a cleaned version with non-secret demo credentials from environment variables or harmless defaults. Ensure GET returns `index.html`, failed login re-renders the form with a message, successful login renders `welcome.html`, and close the Jinja block in `welcome.html`. Add `requirements.txt` with Flask.
- Files to exclude or move to `_excluded_review/`: Move original `app.py` to `_excluded_review/security_review/`; consider moving `Screenshot 2024-09-15 114524.png` and `next steps.txt`.
- README needed: yes
- Recommendation: Keep as a Flask form-validation learning project after removing hardcoded credentials from publishable code and fixing the route/template returns.

## Batch 4 - 2026-05-31

## gitForkPractice
- Suggested name: `flask-socketio-fork-practice`
- Category: Archive
- Language/framework: Python Flask with Flask-SocketIO, HTML/JavaScript; also Git practice material
- Main entry point: `Flask-Sockets/app.py`
- Current status: Source passes syntax-only compile checks. Runtime was not verified because Flask and Flask-SocketIO are not installed in this environment. The nested `Flask-Sockets` app appears similar to the Socket.IO form examples and may run after dependency/security cleanup.
- Problems found: Top-level `.git/` and nested `Flask-Sockets/.git/` should not be published inside `old-projects`. `Flask-Sockets/app.py` contains a hardcoded Flask `SECRET_KEY` placeholder. The folder appears to be fork/Git practice rather than a distinct project. `SecretPython.py` is not actually secret from inspection, but the filename is suspicious and should be reviewed. Existing README is minimal. No root README for the folder.
- Functionality fixes needed: If kept as runnable, move original `Flask-Sockets/app.py` to `_excluded_review/security_review/`, create a cleaned copy using `FLASK_SECRET_KEY`, and add `requirements.txt` with Flask and Flask-SocketIO. Because this appears to be Git/fork practice and duplicates other Socket.IO examples, archiving is recommended.
- Files to exclude or move to `_excluded_review/`: `.git/`, `Flask-Sockets/.git/`, and possibly `Flask-Sockets/SecretPython.py` for review; move original `Flask-Sockets/app.py` to `_excluded_review/security_review/` if producing a publishable cleaned copy.
- README needed: yes
- Recommendation: Archive as Git/fork practice rather than a primary project, unless you specifically want another Socket.IO example kept.

## hopefullast
- Suggested name: `flask-session-login`
- Category: Keep but Rename
- Language/framework: Python Flask with sessions and HTML/CSS/JavaScript
- Main entry point: `app.py`
- Current status: Source passes syntax-only compile checks but appears not runnable as-is. `app = flask.Flask(__name__)` references `flask` without importing the module, `request` and `session` are used but not imported, `wsgi_app == app.wsgi_app` is a comparison instead of assignment, and the port reads `SERVER_HOST` instead of `SERVER_PORT`.
- Problems found: Hardcoded Flask secret in `app.py`; should not be published as-is. No README, `.gitignore`, or `requirements.txt`. `Screenshot 2024-09-15 114524.png` and `next steps.txt` look like reference/notes files rather than source.
- Functionality fixes needed: Move original `app.py` to `_excluded_review/security_review/` and create a cleaned copy with correct imports, `app = Flask(__name__)`, environment-based secret with harmless development fallback, corrected `wsgi_app = app.wsgi_app`, and `SERVER_PORT` handling. Add `requirements.txt` with Flask.
- Files to exclude or move to `_excluded_review/`: Move original `app.py` to `_excluded_review/security_review/`; consider moving `Screenshot 2024-09-15 114524.png` and `next steps.txt`.
- README needed: yes
- Recommendation: Keep as a small Flask session-login learning project after minimal syntax/import/security cleanup.

## loool
- Suggested name: `flask-socketio-chat`
- Category: Keep but Rename
- Language/framework: Python Flask with Flask-SocketIO, HTML/JavaScript
- Main entry point: `app.py`
- Current status: Source passes syntax-only compile checks. Runtime was not verified because Flask and Flask-SocketIO are not installed in this environment. The server-side Socket.IO handlers are present, but the client submit handler appears broken.
- Problems found: Bundled `.venv/` should not go to GitHub. Hardcoded Flask `SECRET_KEY` placeholder in `app.py`; should not be published as-is. No README, project `.gitignore`, or `requirements.txt`. `static/index.js` uses `$("formMessage")` instead of the form selector and sends `$("#message_data").val` instead of calling `.val()`, so messages likely do not emit correctly. `Screenshot 2024-09-15 114524.png` and `next steps.txt` look like reference/notes files rather than source.
- Functionality fixes needed: Move original `app.py` to `_excluded_review/security_review/` and create a cleaned copy using `FLASK_SECRET_KEY`. Fix the form submit selector and `.val()` call in `static/index.js`. Add `requirements.txt` with Flask and Flask-SocketIO.
- Files to exclude or move to `_excluded_review/`: `.venv/`; move original `app.py` to `_excluded_review/security_review/`; consider moving `Screenshot 2024-09-15 114524.png` and `next steps.txt`.
- README needed: yes
- Recommendation: Keep as a Flask-SocketIO chat/message learning project after dependency, secret, and client submit fixes.

## somethingGit
- Suggested name: `git-practice-notes`
- Category: Archive
- Language/framework: Python script plus Git command notes
- Main entry point: `app.py`
- Current status: Runnable only as a trivial script that prints `ASFAS`. This appears to be Git practice notes rather than an application.
- Problems found: Contains a nested `.git/` directory that should not be published inside `old-projects`. README already says it is a test. Existing `.gitignore` present. `gitBasicCommands` is notes rather than application code.
- Functionality fixes needed: None for functionality. If archived, preserve the notes and script as-is.
- Files to exclude or move to `_excluded_review/`: `.git/`.
- README needed: existing README should be updated if archived in this cleanup.
- Recommendation: Archive as Git practice notes, not a runnable coding project.

## sql
- Suggested name: `flask-sql-todo`
- Category: Keep but Rename
- Language/framework: Python Flask with mysql-connector and HTML/CSS templates
- Main entry point: `app.py`
- Current status: Source passes syntax-only compile checks but appears not runnable as-is. `app.py` renders `index.html`, but only `home.html`, `layout.html`, and `edit.html` exist. Templates reference routes like `/add`, `/update/<id>`, and `/delete/<id>` that are not implemented. No database connection code exists beyond importing `mysql.connector`.
- Problems found: No README, `.gitignore`, or `requirements.txt`. `.vscode/` should usually not be published. `Screenshot 2024-09-15 114524.png` and `next steps.txt` look like reference/notes files rather than source. The app is a todo list shell with missing routes and missing DB setup.
- Functionality fixes needed: Minimal option: change `/` to render `home.html` and pass an empty list so the page loads, then document it as partially working. If making the todo workflow run, add basic in-memory list handling or proper database setup; that may be more than a small cleanup and should be avoided unless explicitly approved.
- Files to exclude or move to `_excluded_review/`: `.vscode/`; consider moving `Screenshot 2024-09-15 114524.png` and `next steps.txt`.
- README needed: yes
- Recommendation: Keep as a partially working Flask SQL/todo learning project after making the home page load and documenting missing database-backed routes.
