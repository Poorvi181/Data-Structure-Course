class Student:
    def __init__(self,name,grade,school_name):
        self.name = name
        self.grade = grade
        self.school_name = school_name

    def show_details(self):
        print(f"I am {self.name} from {self.school_name} in grade {self.grade}.")

student1 = Student("John", 8, "Greenwood School")
student2 = Student("Alex", 9, "Riverdale High")

student1.show_details()
student2.show_details()

