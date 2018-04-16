import os
import json
from flask import Flask, render_template, request, redirect, flash, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'some_secret'


#Username validator to ensure all usernames are between 3 and 10 characters and contain no spaces

def username_validator(username):
    if len(username) < 3 or len(username) > 10:
        return False
    else:
        for char in username:
            if char == ' ':
                return False
 
#Add to scoreboard               
def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)

def add_to_scoreboard(username, score):
    write_to_file('data/scoreboard.txt', "{0} {1} {2}\n".format(
            score,
            username,
            datetime.now().strftime("%d/%m/%y")))


#Display scoreboard in ordered fashion and split scores into list for indexing into tables            
def display_scoreboard():
    scoreboard = []
    details =[]
    with open('data/scoreboard.txt', 'r') as score_data:
        scoreboard = score_data.readlines()
        ordered = sorted(scoreboard, key= (lambda line: int(line.lstrip().split(' ')[0])))
        for score in ordered[::-1]:
            details.append(score.split())
        
    return details
 
def get_message(score):
    message = ""
    if score < 3:
        message = "You scored " + str(session["score"]) +"/10. A terrible score"
    elif score < 6:
        message = "You scored " + str(session["score"]) +"/10. A mediocre score"
    elif score < 8: 
        message = "You scored " + str(session["score"]) +"/10. A very average score"
    elif score < 10:
        message = "You scored " + str(session["score"]) +"/10. Close... but no cigar"
    else:
        message = "You scored " + str(session["score"]) +"/10. You have mad Google skills"
        
    return message   

    
#Login page to set session library of username and score
@app.route('/', methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['username'].strip()
        if username_validator(username) == False:
            flash("Username must contain between 3 and 10 characters and cannot contain any spaces")
        else:
            session['username'] = username
            session['score'] = 0
            session['url'] = 1
            return redirect(session['url'])
    return render_template("index.html")
    
#Render riddles with pictures and current score, also protects from users revisiting pages and cheating
@app.route('/<number>', methods=["GET","POST"])
def get_info(number):
    total = str(int(session['url']) - 1)
    if str.isdigit(number):
        if int(number) == session["url"] and int(number) < 11:
            riddle = {}
            with open("data/riddle_data.json", "r") as json_data:
                data = json.load(json_data)
                for obj in data:
                    if obj["url"] == number:
                        riddle = obj
                        
        elif int(number) > 10:
            return redirect('leaderboard')
            
        else:
            return redirect(session["url"])
            
        return render_template("member.html", riddle=riddle, user=session, total=total)
    else:
        return "<h2>This page is unavailable<h2>"
        
        
@app.route('/skip_question', methods=["POST"])
def skip():
    if request.method == 'POST':
        if session['url'] == 10:
            add_to_scoreboard(session['username'], session['score'])
            session['url'] += 1
            return redirect(session['url'])
        else:
            session['url'] += 1
            return redirect(session['url'])
    

#Validate riddle answers, adjust score, if answer incorrect flash message will display incorrect answer and inform 
#of 'pass' option. Will eventually redirect to leaderboard when all questions are answered or passed.
@app.route('/submit_answer', methods = ["POST"])
def check_answer():
    if request.method == 'POST':
        guess = request.form['answer'].strip().title()
        answer = request.form["solution"]
        if session['url'] < 10:
            if guess == answer:
                session['url'] += 1
                session['score'] += 1
                return redirect(session['url'])
            else:
                flash('"{}" is incorrect. Please try again.'.format(request.form['answer']))
                return redirect(session['url'])
                
        elif session['url'] == 10:
            if guess == answer:
                session['url'] += 1
                session['score'] += 1
                add_to_scoreboard(session['username'], session['score'])
                return redirect('leaderboard')
            else:
                flash('"{}" is incorrect. Please try again.'.format(request.form['answer']))
                return redirect(session['url'])
            
            
            
#Display leaderboard 
@app.route('/leaderboard')
def leaderboard():
    if session['username'] != None and session["url"] >= 11:
        message = get_message(session['score'])
        scoreboard = display_scoreboard()
        
        
        return render_template("leaderboard.html", scoreboard=scoreboard, user=session, message=message)
    else:
        message = " "
        scoreboard = display_scoreboard()
        return render_template("leaderboard.html", scoreboard=scoreboard, user=session, message=message)
 
  


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug = True)  