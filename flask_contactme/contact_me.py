from flask import Flask, render_template, request
import smtplib #Import smtp library
from flask_mail import Mail, Message#CS50 flask import

import os


app = Flask(__name__)

@app.route('/')
def main():
    return render_template("flask_contactme.html")


@app.route('/form', methods=['POST'])
def form():
    firstname = request.form.get("First_name")
    lastname = request.form.get("Last_name")
    email = request.form.get("Email")

    msg = request.form.get("msg")

    message = ("NEW MESSAGE! /n", "From: ", firstname, " ", lastname, "/n", "Email: ", email, "/n", "Message: /n", msg)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    title ="Thank you!"
    return render_template("Submission.html", title = title)
if __name__ == '__main__':
    app.run()