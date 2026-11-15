# Multiple inheritance: Teacher + Researcher -> Professor

class Teacher:
    def teach(self):
        print("Teaching students in class.")

class Researcher:
    def research(self):
        print("Doing research work in the lab.")

class Professor(Teacher, Researcher):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am Professor {self.name}.")

prof = Professor("Sharma")
prof.introduce()
prof.teach()
prof.research()
