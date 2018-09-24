from run import app
import unittest
from flask import Flask, session
from quiz_functions import initiate_session

"""I tried running some automated tests. Below is as far as I got, I could only test the login page validation,
 the rendering of the first page of the quiz and the leaderboard page. After this I could not find a way to correctly test the "/submit_answer"
route. I have tested alot of the individual functions I wrote for the routes in test_quiz_functions.py."""

class FlaskTestCase(unittest.TestCase):
    # Test getting the login page and checking the content is correct.
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Riddle Quiz' in response.data)
    
    # Test The login page with valid username and it is correctly redirected.    
    def test_login_valid_username(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(username="tester"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'tester, your score is 0 / 0' in response.data)
        self.assertTrue(b'This thing all things devours: Birds, beasts, trees, flowers; Gnaws iron, bites steel; Grinds hard stones to meal; Slays king, ruins town, And beats high mountain down' in response.data)
    
    # Test The login page with invalid username and check the response message. 
    def test_login_invalid_username(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(username="testecdfsfv2348nn8e"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Username must contain between 3 and 10 characters and cannot contain any spaces' in response.data)
    
    # Test the leaderboard page loads correctly.   
    def test_leaderboard_not_logged_in(self):
        tester = app.test_client(self)
        response = tester.get('/leaderboard_no_login', follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Leaderboard' in response.data)
       
    
        
        
    
        
        
if __name__ == '__main__':
    unittest.main()