def test_are_equal(actual, expected):
    assert actual == expected, "Expected {0}, got {1}".format(expected, actual)

def get_message(score):
    message = ""
    if score < 3:
        message = "A terrible score"
    elif score < 6:
        message = "A mediocre score"
    elif score < 8: 
        message = "Very average"
    elif score < 10:
        message = "Close... but no cigar"
    else:
        message = "You have mad google skills"
        
    return message
        
test_are_equal(get_message(0), "A terrible score") 
test_are_equal(get_message(5), "A mediocre score")
test_are_equal(get_message(6), "Very average")
test_are_equal(get_message(8), "Close... but no cigar")
test_are_equal(get_message(10), "You have mad google skills")

print("all tests passed") 
        