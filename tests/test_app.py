"""
A tiny test suite for the Employee Leave Portal.

Run it locally with:
    python -m pytest -v
"""

import os

import app as app_module


def test_database_is_created():
    """init_db() should create the SQLite file."""
    app_module.init_db()
    assert os.path.exists(app_module.DB_PATH)


def test_index_page_loads():
    """The home page should return HTTP 200."""
    client = app_module.app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_submitting_a_request_works():
    """POSTing the form should create a new leave request."""
    app_module.init_db()
    client = app_module.app.test_client()

    before = len(client.get("/").data)

    response = client.post(
        "/request",
        data={
            "employee_name": "Test User",
            "leave_type": "Sick",
            "start_date": "2026-01-01",
            "end_date": "2026-01-02",
            "reason": "Flu",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    # The page after submitting should contain the new employee name.
    assert b"Test User" in response.data
    assert len(response.data) > before
