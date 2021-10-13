from flask import Flask

app = Flask(__name__)
@app.route('/')

def Contactme():
    return "This is my contact me Page"

if __name__ == '__main__':
    app.run()