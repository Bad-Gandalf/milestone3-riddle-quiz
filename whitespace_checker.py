def test_are_equal(actual, expected):
    assert actual == expected, "Expected {0}, got {1}".format(expected, actual)


def username_validator(username):
    if len(username) > 12:
        return False
    elif len(username) < 3:
        return False
    else:
        for char in username:
            if char == ' ':
                return False
            
test_are_equal(username_validator(""), False) 
test_are_equal(username_validator("po"), False)
test_are_equal(username_validator("pop"), None)
test_are_equal(username_validator("pop3"), None)
test_are_equal(username_validator("pop3 1"), False)
test_are_equal(username_validator("pop3 10"), False)
test_are_equal(username_validator("123456789012"), None)
test_are_equal(username_validator("1234567890123"), False)
        
        
print("all tests passed")       
        
#print ("Usernames cannot contain any spaces")        
    