# Code Institute - Milestone Project 3 - Riddle Me This...
#### by Patrick Doherty

The brief I was given for this project was the following:

#### CREATE A 'RIDDLE-ME-THIS' GUESSING GAME
Build a web application game that asks players to guess the answer to a pictorial or text-based riddle.
The player is presented with an image or text that contains the riddle. Players enter their answer into a textarea and submit their answer using a form.
If a player guesses correctly, they are redirected to the next riddle.
If a player guesses incorrectly, their incorrect guess is stored and printed below the riddle. The textarea is cleared so they can guess again.
Multiple players can play an instance of the game at the same time, each in their own browser. Users are identified by a unique username, but note that no authentication features such as a password are required for this project.
Create a leaderboard that ranks top scores for all (at least recent) users.

#### I completed this brief and on the suggestion of my mentor I went and converted into a one-page app with the use of javascript. If the user's
browser has disabled  javascript it will revert to the normal multi-page app.

## UX
#### User stories
1. User will be directed to a login page and asked for a username, no password neccessary. The username will then be validated with some 
basic criteria. Once a username is acceptable the user will be directed to the first question of the quiz. 
2. The user is presented with a picture and a riddle. They have the option to submit an answer or skip the question. 
3. If the user enters the correct answer they are directed to the next page where their updated total is displayed.
4. If they answer a question incorrectly they will be given an error message and it will remain on the same page until the correct answer is given.
5. If the user chooses to skip the question they will move on to the next question. 
6. Once the user has attempted/skipped 10 questions they will be redirected to the leaderboard which will display a message depending on their score.
7. The leaderboard is accessible even if the user has not logged in, although they will not recieve a message as they have not submitted a score.


## Features

### Existing Features
- Bugs - For raising tickets when a problem is encountered and other users can discuss this in a forum. Priority is given by upvotes.
- Features - Essentially the same as Bugs but for new feature proposals, and replacing upvotes with monetary contributions.
- Blog - Simple blog app detailing updates on Bugs or Features, only developers can create these.
- Cart - Shopping cart app where users can choose a feature and the amount they wish to contribute. 
- Checkout - Processes payments from users.
- Stats - Serializes information from models and uses this to create statistical charts displaying bug/feature/workflow statistics.

### Features Left to Implement
- Quiz - Users can upload quiz questions, if they are approved they can be added to a bank of questions. Users can then take a quiz made from these questions and compare results
on a scoreboard.


## Technologies used:
##### HTML - hypertext markup language
##### CSS - cascading style sheets 
##### Javascript - client side scripting language
##### Python - Programming Language
##### Git Bash & GitHub -for version control and backup of code
##### Bootstrap - A framework for developing responsive, mobile 1st websites.
##### Flask - python web framework


- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation, and allow for AJAX requests.
- 

##### Plugin - Coverage - I needed during my testing of code. It generates reports which show you how much of your code you have tested.


## Testing
## Automated testing
Automated testing was limited but i was able to use it to test in the login functionality, the quiz rendering and the leaderboard page. 
I hit a brick wall when testing a post only route for the answer submissions.




## Credits

### Media


### Acknowledgements
