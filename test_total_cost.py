from total_cost import calculate_total_cost
from total_cost import main
import difflib


def test_calculate_total_cost_1_to_9():
    assert calculate_total_cost(1) == 50
    assert calculate_total_cost(5) == 250
    assert calculate_total_cost(9) == 450

def test_calculate_total_cost_10_to_19():
    assert calculate_total_cost(10) == 450
    assert calculate_total_cost(15) == 675
    assert calculate_total_cost(19) == 855

def test_calculate_total_cost_20_to_29():
    assert calculate_total_cost(20) == 760
    assert calculate_total_cost(25) == 950
    assert calculate_total_cost(29) == 1102

def test_calculate_total_cost_greater_than_29():
    assert calculate_total_cost(30) == 960
    assert calculate_total_cost(50) == 1600


def test_calculate_total_cost_zero_quantity():
    assert calculate_total_cost(0) == 0

def string_similarity(s1, s2):
    # Calculate similarity ratio
    s1 = s1.replace(" ", "").replace("\n", "")
    s2 = s2.replace(" ", "").replace("\n", "")

    similarity_ratio = difflib.SequenceMatcher(None, s1, s2).ratio()
    return similarity_ratio

def test_main(capsys, monkeypatch, printFeedback=True):

    inputs = iter([1,20,50,0])
    expected_output = """Total cost: 50
Total cost: 760
Total cost: 1600
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
        feedback = "\nExpected:\n" + expected_output+"\n\n"
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
        (test_calculate_total_cost_1_to_9,15),
        (test_calculate_total_cost_10_to_19, 15),
        (test_calculate_total_cost_20_to_29, 15),
        (test_calculate_total_cost_greater_than_29,15),
        (test_calculate_total_cost_zero_quantity,15),
        (test_main,25)
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