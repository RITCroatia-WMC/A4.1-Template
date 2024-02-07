from group_characters import is_upper
from group_characters import is_lower
from group_characters import is_digit
from group_characters import group_characters
from group_characters import main

import difflib
import pytest



def test_is_upper_1():
    assert is_upper('A') is True
    assert is_upper('Z') is True

def test_is_upper_2():
    assert is_upper('a') is False
    assert is_upper('z') is False

def test_is_upper_3():
    assert is_upper('1') is False
    assert is_upper('!') is False
    assert is_upper(' ') is False


def test_lowercase_1():
    assert is_lower('a') is True
    assert is_lower('z') is True

def test_lowercase_2():
    assert is_lower('A') is False
    assert is_lower('Z') is False

def test_lowercase_3():
    assert is_lower('1') is False
    assert is_lower('!') is False
    assert is_lower(' ') is False


def test_digit_1():
    assert is_digit('0') is True
    assert is_digit('5') is True
    assert is_digit('9') is True

def test_digit_2():
    assert is_digit('A') is False
    assert is_digit('z') is False
    assert is_digit('!') is False
    assert is_digit(' ') is False


def test_group_characters_all_digits():
    assert group_characters('12345') == '12345'

def test_group_characters_all_lowercase():
    assert group_characters('abcdef') == 'abcdef'

def test_group_characters_all_uppercase():
    assert group_characters('XYZ') == 'XYZ'

def test_group_characters_mixed_characters_1():
    assert group_characters('a6Bt233GqrY7') == '62337atqrBGY'

def test_group_characters_mixed_characters_2():
    assert group_characters('aAaAaAaA') == 'aaaaAAAA'



def string_similarity(s1, s2):
    # Calculate similarity ratio
    s1 = s1.replace(" ", "").replace("\n", "")
    s2 = s2.replace(" ", "").replace("\n", "")

    similarity_ratio = difflib.SequenceMatcher(None, s1, s2).ratio()
    return similarity_ratio


def test_main(capsys, monkeypatch, printFeedback=True):

    inputs = iter(["ABC","a6Bt233GqrY7",""])
    expected_output = """ABC
62337atqrBGY
Goodbye!"""
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
   
    # Execute the function
      # Run the main function
    main()
    #Get the feedback
    captured = capsys.readouterr()

    similarity_threshold = 0.95  # Set your desired threshold here

    similarity_score = string_similarity(expected_output, captured.out)

   
    if similarity_score >= similarity_threshold:
        feedback = "Strings are similar enough (score: {0:.2f}%). Test passed!".format(similarity_score * 100)
    else:
        feedback = "Expected:\n" + expected_output+"\n\n"
        feedback = feedback + "\nCaptured:\n" + captured.out
    # Use sys.stdout to write out the feedback message
    if(printFeedback):
        print(feedback + "\n")

    assert similarity_score >= similarity_threshold, f"Strings are not similar enough (score: {similarity_score})"


    ##RUN WITH THIS pytest --tb=short -s test_main.py


def test_FinalGrade(capsys, monkeypatch):
    
    totalPoints = 0

    ## CALL the testers, do not print, otherwise you will mess with some of the testers
  
    test_functions = [
        (test_is_upper_1, 6),
        (test_is_upper_2, 6),
        (test_is_upper_3, 6),
        (test_lowercase_1, 6),
        (test_lowercase_2, 6),
        (test_lowercase_3, 6),
        (test_digit_1, 6),
        (test_digit_2, 6),
        (test_group_characters_all_digits, 6),
        (test_group_characters_all_lowercase, 6),
        (test_group_characters_all_uppercase, 6),
        (test_group_characters_mixed_characters_1, 6),
        (test_group_characters_mixed_characters_2, 6),
        (test_main,22)
    ]
     

    outputFeedbac = "############ TOTAL POINTS ###################\n"
    
    for function, point in test_functions:
        if function.__name__=="test_main":#SPECIAL CASE
            try:
                function(capsys,monkeypatch,False)
                outputFeedbac=outputFeedbac+f"PASS:{function.__name__}: {point}"+"\n"
                totalPoints += point
            except AssertionError:
                outputFeedbac=outputFeedbac+f"FAIL:{function.__name__}: {0}\n"
        else:
            try:
                function()
                outputFeedbac=outputFeedbac+f"PASS:{function.__name__}: {point}"+"\n"
                totalPoints += point
            except AssertionError:
                outputFeedbac=outputFeedbac+f"FAIL:{function.__name__}: {0}\n"
    
    print(outputFeedbac)
    print("Total points",totalPoints)
    assert True