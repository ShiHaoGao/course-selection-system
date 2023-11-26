# app/routes.py
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Course, Enrollment


@app.route("/")
def index():
    courses = Course.query.all()
    return render_template("index.html", courses=courses)


@app.route("/enroll/<int:course_id>")
def enroll(course_id):
    course = Course.query.get(course_id)
    if course:
        return render_template("enroll.html", course=course)
    return redirect(url_for("index"))


@app.route("/process_enrollment/<int:course_id>", methods=["POST"])
def process_enrollment(course_id):
    course = Course.query.get(course_id)
    if course:
        student_name = request.form.get("student_name")
        enrollment = Enrollment(student_name=student_name, course=course)
        db.session.add(enrollment)
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/cancel_enrollment/<int:enrollment_id>")
def cancel_enrollment(enrollment_id):
    enrollment = Enrollment.query.get(enrollment_id)
    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/modify_enrollment/<int:enrollment_id>", methods=["GET", "POST"])
def modify_enrollment(enrollment_id):
    enrollment = Enrollment.query.get(enrollment_id)
    if request.method == "POST":
        if enrollment:
            enrollment.student_name = request.form.get("student_name")
            db.session.commit()
        return redirect(url_for("index"))
    return render_template("modify_enrollment.html", enrollment=enrollment)
