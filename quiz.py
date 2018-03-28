import json 
from datetime import datetime

def get_username():
    username = input("Please select a username: ")
    username = str(username.title())
    return username
    
def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)
        
def add_to_scoreboard(username, score):
    write_to_file('data/scoreboard.txt', "{0} {1} - {2}\n".format(
            score,
            username.title(),
            datetime.now().strftime("%d/%m/%y - %H:%M:%S")))
    
def display_scoreboard():
    scoreboard = []
    with open('data/scoreboard.txt', 'r') as score_data:
        scoreboard = score_data.readlines()
    ordered = sorted(scoreboard, key= (lambda line: int(line.lstrip().split(' ')[0])))
    for score in ordered[::-1]:
        print (score)
    
    
def get_riddles():
    riddles = []
    with open('data/riddle_data.json', "r") as json_data:
        riddles = json.load(json_data)
        
            
    return riddles

def get_pictures():
    pictures = {}
    with open('data/riddle_data.json', "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            pictures.update({data[obj]["riddle"] : data[obj]["image_source"]})
    return pictures  
    
def get_url():
    urls = {}
    with open('data/riddle_data.json', "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            urls.update({data[obj]["riddle"] : data[obj]["url"]})
    return urls  

def quiz():
    username = get_username()
    print("Hello " + str(username) + "\nWe have some riddles for you!")
    score = 0
    riddles = get_riddles()
    for i in riddles:
        riddle = riddles[i]['riddle']
        answer = riddles[i]['answer']
        guess = input("" + riddle + ": ").title()
        if guess == answer:
            score += 1
            print ("Correct!\n")
            
        elif guess == "Pass":
            print("You have chosen to pass this question\n")
        else:
            while guess != answer:
                print("Incorrect, please try again.\n")
                guess = input("" + riddle + ": ").title()
                if guess == answer:
                    score += 1
                    print("Correct!\n")
                    
                elif guess == "Pass":
                    print("You have chosen to pass this question\n")
                    break

    print(str(username) + ", you got " + str(score) +"/10 correct\n") 
    add_to_scoreboard(username, score)
    display_scoreboard()
       
print(quiz())    
