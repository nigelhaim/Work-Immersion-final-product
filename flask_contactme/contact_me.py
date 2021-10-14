from flask import Flask, render_template, request
import smtplib #Import smtp library
import os


app = Flask(__name__)

e_user = os.environ.get("ENCRYPT_USER")
e_pass = os.environ.get("ENCRYPT_PASS")
to_user = os.environ.get("TO_USER")

@app.route('/')
def main():
    return render_template("flask_contactme.html")


@app.route('/form', methods=["POST"])
def form():
    firstname = request.form.get("First_name")
    lastname = request.form.get("Last_name")
    email = request.form.get("Email")

    mess = request.form["message_1"]

    msg = ("NEW MESSAGE! /n")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(e_user, e_pass)
    server.sendmail(e_user, to_user, "NEW MESSAGE! /n")
    
    title ="Thank you!"
    return render_template("Submission.html", title = title)
if __name__ == '__main__':
    app.run()