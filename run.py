import os
import json
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
    
@app.route('/riddles/<number>')
def riddle_number(number):
    member = {}
    
    with open("data/riddle_data.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == number:
                member = obj
                
        return render_template("riddles.html", member=riddle_url)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug = True)