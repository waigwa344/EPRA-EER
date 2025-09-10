from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this for production

# ----------------------
# Simple user simulation
# ----------------------
USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "facility1": {"password": "facility123", "role": "facility"}
}

# ----------------------
# Login required decorator
# ----------------------
def login_required(role=None):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if "user" not in session:
                flash("Login required!", "danger")
                return redirect(url_for("home"))
            if role and session.get("role") != role:
                flash("Access denied!", "danger")
                return redirect(url_for("home"))
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

# ----------------------
# Routes
# ----------------------
@app.route("/")
def home():
    return render_template("home.html")  # Landing page with Admin/Facility login buttons

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = USERS.get(username)
        if user and user["password"] == password:
            session["user"] = username
            session["role"] = user["role"]
            if user["role"] == "admin":
                return redirect(url_for("admin_dashboard"))
            else:
                return redirect(url_for("facility_dashboard"))
        flash("Invalid credentials!", "danger")
    return render_template("login.html")  # Can be a generic login template

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for("home"))

# ----------------------
# Admin Dashboard
# ----------------------
@app.route("/admin")
@login_required(role="admin")
def admin_dashboard():
    return render_template("admin_dashboard.html")

# ----------------------
# Facility Dashboard
# ----------------------
@app.route("/facility")
@login_required(role="facility")
def facility_dashboard():
    return render_template("facility_dashboard.html")

# ----------------------
# Run
# ----------------------
if __name__ == "__main__":
    app.run(debug=True)
