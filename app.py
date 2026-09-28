from flask import Flask

app = Flask(__name__)

@app.route('/')
def accueil():
    return '<h1>Mon College</h1><p>Application en marche !</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
