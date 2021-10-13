from flask import Flask, render_template

app = Flask(__name__)

@app.route('/contact')
def contact():
    title = "Contact me"
    return render_template("https://nigelhaim.github.io/Work-Immersion-final-product/Flask_contact/contactme_flask.html")

    if __name__ == "__main__":
        app.run()