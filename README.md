# 🌴 Employee Leave Portal

A small, beginner-friendly **Employee Leave Management** web application.

Employees can:
- ✅ Submit a leave request (name, type, dates, reason)
- ✅ View all leave requests in a list with their status

The project is kept **simple** and easy to read so it is a good base to
learn and build on.

---

## 🧰 Tech stack

| Layer        | Choice                                      |
|--------------|---------------------------------------------|
| Language     | Python 3.11                                 |
| Web framework| [Flask](https://flask.palletsprojects.com/) |
| Database     | SQLite (file-based, no server to install)   |
| UI           | Plain HTML + CSS                            |

---

## 📁 Project structure

```
Employee-Portal/
├── app.py                # Flask app: routes + SQLite logic
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignore caches, venv, local DB
├── templates/
│   ├── base.html         # Shared page layout
│   └── index.html        # Form + leave request table
├── static/
│   └── style.css         # Clean styling
└── tests/
    └── test_app.py       # Small pytest suite
```

---

## 🚀 Run the app locally

You need **Python 3.11+** installed.

```bash
# 1. (Optional but recommended) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Open **http://localhost:5000** in your browser.

> The SQLite database is created automatically at `data/leaves.db` on first run.

---

## ✅ Running the tests

The `tests/` folder contains a small pytest suite. Run it with:

```bash
pip install -r requirements.txt
python -m pytest -v
```

---

## 📝 Notes

- This is a learning project: there is **no login/authentication** and anyone
  can submit requests. Adding auth is a good next exercise.
- Leave requests start with status **Pending** (shown as a badge). Adding
  approve/reject buttons is a nice feature to practice next.
- SQLite is perfect for learning but not ideal for many concurrent users;
  you can move to a database like PostgreSQL later if you want.

Enjoy building! 🚀
