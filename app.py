from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import json

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session handling

# -------------------------------
# Dummy credentials (replace with your own)
# -------------------------------
ADMIN_CREDENTIALS = {"username": "admin", "password": "admin123"}
FACILITY_CREDENTIALS = {"username": "facility", "password": "facility123"}

# -------------------------------
# Home page
# -------------------------------
@app.route("/")
def home():
    return render_template("home.html")

# -------------------------------
# Admin Login
# -------------------------------
@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == ADMIN_CREDENTIALS["username"] and password == ADMIN_CREDENTIALS["password"]:
            session["user"] = "admin"
            return redirect(url_for("admin_dashboard"))
        else:
            return render_template("admin_login.html", error="Invalid credentials")
    return render_template("admin_login.html")

# -------------------------------
# Facility Login
# -------------------------------
@app.route("/facility_login", methods=["GET", "POST"])
def facility_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == FACILITY_CREDENTIALS["username"] and password == FACILITY_CREDENTIALS["password"]:
            session["user"] = "facility"
            return redirect(url_for("facility_dashboard"))
        else:
            return render_template("facility_login.html", error="Invalid credentials")
    return render_template("facility_login.html")

# -------------------------------
# Admin Dashboard
# -------------------------------
@app.route("/admin_dashboard")
def admin_dashboard():
    if session.get("user") != "admin":
        return redirect(url_for("admin_login"))

    # Example Excel/EER integration
    # Replace this with your actual EER system code
    # Here we create a dummy dataframe
    df = pd.DataFrame({
        "Facility": ["A", "B", "C"],
        "Energy_Consumption": [100, 150, 200],
        "Energy_Production": [120, 130, 210],
        "EER": [1.2, 0.87, 1.05]
    })
    data_json = df.to_dict(orient="records")  # For JS usage in dashboard

    return render_template(
        "admin_dashboard.html",
        tables=df.to_html(classes="table table-bordered", index=False),
        data_json=json.dumps(data_json)
    )

# -------------------------------
# Facility Dashboard
# -------------------------------
@app.route("/facility_dashboard")
def facility_dashboard():
    if session.get("user") != "facility":
        return redirect(url_for("facility_login"))
    return render_template("facility_dashboard.html")

# -------------------------------
# Logout
# -------------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

# -------------------------------
# Run Flask
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
