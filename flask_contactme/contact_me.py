from flask import Flask, render_template, request, redirect
import smtplib #Import smtp library
from flask_mail import Mail, Message#CS50 flask import

import os


app = Flask(__name__)

@app.route('/')
def main():
    return render_template("flask_contactme.html")


@app.route('/form', methods=['POST'])
def form():
    title ="Thank you!"
    return render_template("Submission.html", title = title)
if __name__ == '__main__':
    app.run()