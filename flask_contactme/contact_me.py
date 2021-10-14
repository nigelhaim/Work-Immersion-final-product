from flask import Flask, render_template, request
import smtplib #Import smtp library
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)
e_user = os.getenv('ENCYPT_USER')
e_pass = os.getenv('ENCRYPT_PASS')
to_user = os.getenv('TO_USER')

@app.route('/')
def main():
    return render_template("flask_contactme.html")


@app.route('/form', methods=["POST"])
def form():
    firstname = request.form.get("First_name")
    lastname = request.form.get("Last_name")
    email = request.form.get("Email")
    space = " "
    mess = request.form["message_1"]
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(e_user, e_pass)
    server.sendmail(e_user, to_user, ("New message!\n" + "From: " + firstname + " " + lastname + "\n"+ "Email:" + email + "\n" + "Message:\n" + "\n" + mess ))
    
    title ="Thank you!"
    return render_template("Submission.html", title = title)
if __name__ == '__main__':
    app.run()