from quiz_functions import *

app = Flask(__name__)
app.secret_key = 'some_secret'
score_data = 'data/scoreboard.txt'
riddle_json = 'data/riddle_data.json'

#Set the messages you want to appear when quiz is completed based on score
def get_message(score):
    message = ""
    if session['url'] > 10:
        if score < 3:
            message = "You scored " + str(session["score"]) +"/10. Terrible"
        elif score < 6:
            message = "You scored " + str(session["score"]) +"/10. Mediocre"
        elif score < 8: 
            message = "You scored " + str(session["score"]) +"/10. Above average"
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
            initiate_session(username)
            return redirect(url_for('quiz'))
    return render_template("index.html")
    
#Login page to set session library of username and score  - for use with javascript supported browsers
@app.route('/js_login', methods = ["GET","POST"])
def js_login():
    if request.method == "POST":
        username = request.form['username'].strip()
        if username_validator(username) == False:
            flash("Username must contain between 3 and 10 characters and cannot contain any spaces")
            return render_template("index.html")
        else:
            initiate_session(username)
            total = questions_asked(session['url'])
            riddle = match_page_info_with_url(riddle_json, session['url'])
            return render_template("quiz_js.html", riddle=riddle, user=session, total=total)
    
    
#Render riddles with pictures and current score
@app.route('/quiz')
def quiz():
    total = questions_asked(session['url'])
    riddle = match_page_info_with_url(riddle_json, session['url'])
    if session['url'] > 10:
        return redirect('leaderboard')
        
    return render_template("member.html", riddle=riddle, user=session, total=total)

#Validate riddle answers, adjust score, if answer incorrect flash message will display incorrect answer 
#Will eventually redirect to leaderboard when all questions are answered or passed.

@app.route('/submit_answer', methods = ["GET","POST"])
def submit_answer():
    if request.method == 'POST':
        guess = request.form['answer'].strip().title()
        answer = request.form["solution"]
        if session['url'] < 10:
            if guess == answer:
                increment_url_and_score(1, 1)
            else:
                flash('"{}" is incorrect. Please try again.'.format(request.form['answer']))
        
        elif session['url'] == 10:
            if guess == answer:
                increment_url_and_score(1, 1)
                add_to_scoreboard(session['username'], session['score'], score_data)
            else:
                flash('"{}" is incorrect. Please try again.'.format(request.form['answer']))
                
        else:
            return redirect('leaderboard')
    
    return redirect(url_for('quiz'))   

#For js supporting browsers
#Validate riddle answers, adjust score, if answer incorrect flash message will display incorrect answer 
#Will eventually redirect to leaderboard when all questions are answered or passed.
@app.route('/js_submit_answer' , methods=["POST"])
def js_submit_answer():
    if request.method == "POST":
        guess = request.form["answer"]
        guess = guess.strip().title()
        answer = request.form["solution"]
        if session['url'] < 10:
            if guess == answer:
                increment_url_and_score(1, 1)
            else:
                flash('"{}" is incorrect. Please try again.'.format(request.form['answer']))
        
        elif session['url'] == 10:
            if guess == answer:
                increment_url_and_score(1, 1)
                add_to_scoreboard(session['username'], session['score'], score_data)
                scores = get_scoreboard_data(score_data)
                message = get_message(session['score']) 
                return render_template('leaderboard_js.html', scores=scores, user=session, message=message)
        
            else:
                flash('"{}" is incorrect. Please try again.'.format(request.form['answer']))
                
        total = questions_asked(session['url'])
        riddle = match_page_info_with_url(riddle_json, session['url'])
        return render_template("quiz_js.html", riddle=riddle, user=session, total=total)

#Skip button included to skip over question and still increment the session url by 1       
@app.route('/skip_question', methods=["POST"])
def skip_question():
    if request.method == 'POST':
        if session['url'] == 10:
            increment_url_and_score(1, 0)
            add_to_scoreboard(session['username'], session['score'], score_data)
            return redirect('leaderboard')
        else:
            increment_url_and_score(1, 0)
    return redirect(url_for('quiz'))
    
#Skip button included to skip over question and still increment the session url by 1 - JS supported browsers   
@app.route('/js_skip_question', methods=["POST"])
def js_skip_question():
    if request.method == "POST":
        if session['url'] == 10:
            increment_url_and_score(1, 0)
            add_to_scoreboard(session['username'], session['score'], score_data)
            scores = get_scoreboard_data(score_data)
            message = get_message(session['score']) 
            return render_template('leaderboard_js.html', scores=scores, user=session, message=message)
        else:
            increment_url_and_score(1, 0)
            total = questions_asked(session['url'])
            riddle = match_page_info_with_url(riddle_json, session['url'])
            return render_template("quiz_js.html", riddle=riddle, user=session, total=total)

        
#Display leaderboard 
@app.route('/leaderboard')
def leaderboard():
    scores = get_scoreboard_data(score_data)
    message = get_message(session['score']) 
    return render_template("leaderboard.html", scores=scores, user=session, message=message)
   
@app.route('/leaderboard_no_login')
def leaderboard_no_login():
    scores = get_scoreboard_data(score_data)
    message = " "
    return render_template("leaderboard.html", scores=scores, user=session, message=message)
    
@app.route('/js_leaderboard_no_login')
def js_leaderboard_no_login():
    scores = get_scoreboard_data(score_data)
    message = " "
    return render_template("leaderboard2_js.html", scores=scores, user=session, message=message)
       
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug = True)  