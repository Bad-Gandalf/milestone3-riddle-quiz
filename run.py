import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")
    
@app.route('/riddles')
def riddles():
    return render_template("riddles.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug = True)