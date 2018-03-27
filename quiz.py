import json 

def get_username():
    username = raw_input("Please select a username: ")
    username = str(username)
    print (username)
    
def get_riddles():
    riddles = {}
    with open('data/riddle_data.json', "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            riddles.update({data[obj]["riddle"] : data[obj]["answer"]})
    return riddles
    

def ask_riddles():
    score = 0
    riddles = get_riddles()
    for key in riddles:
        riddle = key
        guess = input("" + riddle + ": ").title()
        if guess == riddles[key]:
            score += 1
            print ("Correct!")
        elif guess == "Pass":
            print("You have chosen to pass this question")
        else:
            while guess != riddles[key]:
                print("Incorrect, please try again.")
                guess = input("" + riddle + ": ").title()
                if guess == riddles[key]:
                    score += 1
                    print("Correct!")
                elif guess == "Pass":
                    print("You have chosen to pass this question")
                    break
                    
            
                
            
    return "You got " + str(score) +"/10 correct"    
    
print (ask_riddles())