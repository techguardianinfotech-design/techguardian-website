from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/terms")   # ✅ THIS WAS MISSING
def terms():
    return render_template("terms.html")

@main.route("/privacy")   # ✅ THIS WAS MISSING
def privacy():
    return render_template("privacy.html")

@main.route("/services")   # ✅ THIS WAS MISSING
def services():
    return render_template("services.html")

@main.route("/website-development")   # ✅ THIS WAS MISSING
def website_development():
    return render_template("website-development.html")

@main.route("/custom-software")
def custom_software():
    return render_template("custom-software.html")

@main.route("/cloud-solutions")
def cloud_solutions():
    return render_template("cloud-solutions.html")

@main.route("/digital-security")
def digital_security():
    return render_template("digital-security.html")

@main.route("/thank-you")
def thank_you():
    return render_template("thank-you.html")

@main.route("/our-team")
def our_team():
    return render_template("our-team.html")



@main.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")

    print("---- NEW LEAD ----")
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)
    print("Message:", message)
    print("------------------")

    return redirect(url_for("main.index"))
