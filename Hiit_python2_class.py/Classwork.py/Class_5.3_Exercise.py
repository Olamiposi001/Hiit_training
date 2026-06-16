from Class_5_modules import compute_grade
"""
Write a program that does grading for scores entered:
1.) Ask the user to enter the number of courses:
2.) per course ask for course code and the score
3.) Display the results of the courses and their course code. E.g

CSC101 - 65 - B
CSC111 - 70 - A

NOTE:
A: 70 - 100
B: 60 - 69
C: 50 - 59
D: 45 - 49
E: 40 - 44
F: 0 - 39
"""


num_of_courses = int(input("Enter the Number of Courses: "))
course_list = []
for n in range(num_of_courses):
    course_code = input(f"Enter the course code_{n+1}: ")
    score = int(input(f"Enter the score_{n+1}: "))
    grade = compute_grade(score)
    course = {"code": course_code, "score": score, "grade": grade}
    course_list.append(course)


for course in course_list:
    print(f"{course['code']} - {course['score']} - {course['grade']}")
