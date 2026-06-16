#  A module is a python file containing reusable codes


def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def subtract(a, b):
    return a-b

MY_NAME = "TONY-AKINLOSOTU"

def compute_grade(score):
    if score >= 70 and score <= 100:
        grade = "A"
    elif score >= 60 and score < 70:
        grade = "B"
    elif score >= 50 and score < 60:
        grade = "C"
    elif score >= 45 and score < 50:
        grade = "D"
    elif score >= 40 and score < 45:
        grade = "E"
    elif score >= 0 and score < 40:
        grade = "F"
    else:
        grade = "The score is invalid"
        
    return grade
        
        
        