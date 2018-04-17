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
            initiate_session(username)
            return redirect(session['url'])
    return render_template("index.html")
    
#Render riddles with pictures and current score, also protects from users revisiting pages and cheating
@app.route('/<number>', methods=["GET","POST"])
def get_info(number):
    total = questions_asked(session['url'])
    if str.isdigit(number):
        if int(number) == session["url"] and int(number) < 11:
            riddle = match_page_info_with_url(riddle_json, number)
        elif int(number) >= 11:
            return redirect('leaderboard')
        else:
            return redirect(session["url"])
        return render_template("member.html", riddle=riddle, user=session, total=total)
    else:
        return render_template("page_unavailable.html")
        
 #Skip button included to skip over question and still increment the session url by 1       
@app.route('/skip_question', methods=["POST"])
def skip():
    if request.method == 'POST':
        if session['url'] == 10:
            add_to_scoreboard(session['username'], session['score'], score_data)
            increment_url_score(1, 0)
            return redirect(session['url'])
        else:
            increment_url_score(1, 0)
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
                increment_url_score(1, 1)
                return redirect(session['url'])
            else:
                flash('"{}" is incorrect. Please try again.'.format(request.form['answer']))
                return redirect(session['url'])
                
        elif session['url'] == 10:
            if guess == answer:
                increment_url_score(1, 1)
                add_to_scoreboard(session['username'], session['score'], score_data)
                return redirect('leaderboard')
            else:
                flash('"{}" is incorrect. Please try again.'.format(request.form['answer']))
                return redirect(session['url'])
            
            
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
       
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug = True)  