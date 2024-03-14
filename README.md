# FlashCards
Personal project - Web APP that will help students with memorization

Structure
FlashCards/  (repo)
├── flashcards/  (Django project directory)
│   ├── accounts/  (app for user accounts)
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── decks/  (app for card decks)
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── flashcards/  (app for flash cards and learning games)
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── static/
│   ├── templates/
│   ├── db.sqlite3
│   ├── manage.py
├── handlers/  (your current python code - before Django setup)
│   └── flashCardLogic.py
└── readme.md


The FlashCards/ directory remains the repository root.
Inside FlashCards/, you have a flashcards/ directory which serves as the Django project directory.
Within the flashcards/ directory, you have separate Django apps for different functionalities of your project:
accounts/: Handles user accounts.
decks/: Manages card decks.
flashcards/: Deals with flash cards and interactive learning games.
Each app (accounts/, decks/, flashcards/) contains its own migrations/ directory for database migrations, templates/ for HTML templates, and relevant Python files (models.py, views.py, etc.).
There's a static/ directory for static files (like CSS, JavaScript, etc.).
db.sqlite3 is the database file.
manage.py remains at the project root for managing Django commands.
Your existing handlers/ directory can stay as it is if it contains unrelated Python code.