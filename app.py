```python
import os
import logging

import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")
if not app.secret_key:
    raise RuntimeError("SECRET_KEY environment variable is required")


def get_db_connection():
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        port=int(os.environ.get("DB_PORT", "3306")),
        connection_timeout=5
    )


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if not name or len(name) > 100 or not email or len(email) > 254:
            flash("Please enter a valid name and email.", "error")
            return redirect(url_for("index"))

        connection = None
        cursor = None

        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO students (name, email) VALUES (%s, %s)",
                (name, email)
            )
            connection.commit()
            flash("Student registered successfully!", "success")

        except Exception:
            app.logger.exception("Could not register student")
            flash("Unable to save student. Check database configuration.", "error")

        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()

        return redirect(url_for("index"))

    students = []
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, name, email FROM students ORDER BY id DESC"
        )
        students = cursor.fetchall()

    except Exception:
        app.logger.exception("Could not retrieve students")
        flash("Database unavailable. Check database configuration.", "error")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
```
