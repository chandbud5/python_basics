#We will see
# 1.Creating class and object
# 2.Calling methods for an object
# 3.Types of variables Instance,Static
# 4.Types of methods instance, static, class

class Student: # Creating class

    school = "City public school" # This is a class (static) variable all object have same value

    def __init__(self,name,rollno): # This __init method works as constructor
        self.name = name        # Name and Rollno are Instance variable all objects can have different values
        self.rollno = rollno

    def show(self): # Defining method to display details about student
        print("Showing details about student name {} is and rollno. is {} ".format(self.name,self.rollno))

    def compare(self,other): # We have created this method to compare two objects whether they are same or not
        if self.name == other.name and self.rollno == other.rollno:
            print("They are Same")
        else:
            print("They are Different")


    @classmethod      # creating class method
    def getschool(cls):
        print(cls.school)

    @staticmethod   # creating static method
    def info():
        print("This is a student class")

student1 = Student('Chand',5) # Creating object of Student class with name student1
student1.show() # calling show method for student1 object

student2 = Student('Chand',5)
student2.show()

student3 = Student('ABC',7)
student3.show()

print("Comparing student1 and student2 ", end="")
student1.compare(student2)
print("Comparing student2 and student3 ", end="")
student2.compare(student3)

print(Student.school+"\n") # printing class(Static) variable

Student.getschool()     # calling classmethod
print("This was from class method\n")

Student.info()  #calling staticmethod
print("This was from static method")