class Students:
    def __init__(self, F, L, D, A):
        self.first_name = F
        self.last_name = L
        self.department = D
        self.age = A
        
    def get_full_name(self):
        print(f"Full name: {self.last_name} {self.first_name}")

student_1 = Students(D="cybersecurity", F="Olamiposi", L="Komolafe", A=42)

print(f"My name is {student_1.last_name} {student_1.first_name}, I am in the {student_1.department} department and I am {student_1.age}yrs")
print("")
student_1.get_full_name()