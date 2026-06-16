# Write a python that tells the user their grade in a particular course:
# 1.) Collect the course code from the user
# 2.) Collect the score from the user
# 3.) Display the Course code, score and the grade i.e CSC 101 - 65 - B
# NOTE: The grading system is as follows:
# 70 - 100 = A
# 60 - 69 = B
# 50 - 59 = C
# 45 - 49 = D
# 40 - 44 = E
# 0 - 39 = F


course_code = input("Enter your course code: ")

score = int(input("Enter your score: "))

user_grade = {}

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
    print("The score is invalid")
"""
user_grade["Course_code"] = course_code
user_grade["Score"] = score
user_grade["Grade"] = grade

print(user_grade)
"""

print(f"\n{course_code} - {score} - {grade}")

"""
if score_str.isdigit():
    score = int(score_str)
    
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
        print("The score only ranges from 0 - 100")
else:
    print("The score is invalid")
"""