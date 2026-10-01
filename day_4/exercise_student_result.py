#define student class with logic
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def result(self):
        if self.marks >=50:
            return f"{self.name} has passed"
        else:
            return f"{self.name} has failed"
s1 =Student("Anita", 45)
print(s1.result())
s2 =Student("Pragya", 95)  
print(s2.result())
s3 =Student("Sita", 40) 
print(s3.result())   





