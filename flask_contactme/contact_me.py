from flask import Flask, render_template, request
import smtplib #Import smtp library
from flask_mail import Mail, Message#CS50 flask import
 
from flask.wrappers import Request
import os
app = Flask(__name__)


app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
app.config["MAIL_PASSWORD"] = os.getenv("UNCRACKABLE_PASS")
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("UNCRACKABLE_EMAIL")

mail = Mail(app)
@app.route('/')
def main():
    return render_template("flask_contactme.html")


@app.route('/form', methods="[POST]")
def form():
    firstname = Request.form.get("First_name")
    lastname = Request.form.get("Last_name")
    email = Request.form.get("Email")

    msg = Request.form.get("msg")
    myemail = "UNCRACKABLE_EMAIL"
    message = Message("NEW MESSAGE!", recipients=[myemail])
    mail.send(message)
if __name__ == '__main__':
    app.run()