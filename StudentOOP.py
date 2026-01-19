class Student:
    def __init__(self,name,marks):
        self.__marks = marks
        self.name = name

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid Marks!!")

    def display(self):
        print("Name", self.name)
        print("Marks: ", self.__marks)

s1=Student("Poorvi", 98)
s1.display()

s1.set_marks(95)
s1.display()        