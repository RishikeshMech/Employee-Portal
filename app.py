"""
Employee Leave Management - Flask backend
------------------------------------------------
A small, beginner-friendly web app that lets employees submit leave
requests and view all requests in a list.

Tech used:
  - Flask      -> web framework (handles routes / pages)
  - SQLite     -> simple file-based database (no server needed)
  - HTML/CSS   -> the user interface

This single file is intentionally kept simple so it is easy to read
and learn from.
"""

import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# ---------------------------------------------------------------------------
# Basic setup
# ---------------------------------------------------------------------------
# We store the SQLite database inside a "data" folder so it is easy to
# find and keep separate from the application code.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "leaves.db")

# Create the Flask app.
# debug=True auto-reloads the server when you change the code (handy for
# local development). In production you should set this to False.
app = Flask(__name__)
app.config["DEBUG"] = os.environ.get("FLASK_DEBUG", "True").lower() == "true"


# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------
def init_db():
    """Create the database and the leave_requests table if they don't exist."""
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS leave_requests (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_name TEXT NOT NULL,
            leave_type    TEXT NOT NULL,
            start_date    TEXT NOT NULL,
            end_date      TEXT NOT NULL,
            reason        TEXT,
            status        TEXT NOT NULL DEFAULT 'Pending',
            created_at    TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


# ---------------------------------------------------------------------------
# Routes (the "pages" of the app)
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    """Show the form and the list of all leave requests."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Show newest requests first.
    cursor.execute("SELECT * FROM leave_requests ORDER BY created_at DESC")
    requests = cursor.fetchall()
    conn.close()
    return render_template("index.html", requests=requests)


@app.route("/request", methods=["POST"])
def add_request():
    """Receive the submitted form and save a new leave request."""
    employee_name = request.form["employee_name"]
    leave_type = request.form["leave_type"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    reason = request.form.get("reason", "")

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO leave_requests
            (employee_name, leave_type, start_date, end_date, reason, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (employee_name, leave_type, start_date, end_date, reason, "Pending", created_at),
    )
    conn.commit()
    conn.close()

    # Send the user back to the home page so they can see the new request.
    return redirect(url_for("index"))


# ---------------------------------------------------------------------------
# Run the app
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    init_db()
    # host="0.0.0.0" makes the app reachable from other machines on the
    # network (not just this computer), which is handy when running it on a
    # remote/Linux server later.
    app.run(host="0.0.0.0", port=5000)
