student = {
    "name": "Ade",
    "score" : 45
}


if student["score"] > 50:
    print(f"{student['name']} has passed the exam")
elif student["score"] == 50:
    print(f"{student['name']} has just passed the exam with an average score")
else:
    print(f"{student['name']} has failed the exam")
    
    
students = [
    {"name" : "kola", "score": 40, "age": 18},
    {"name" : "Tolu", "score": 70, "age": 17},
    {"name" : "Samuel", "score": 40, "age": 20},        
    {"name" : "julia", "score": 30, "age": 17},
]