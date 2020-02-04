# We have outer class as Student and inner class as Laptop

class Student:

    def __init__(self,name):
        self.name = name
        print("Creating an object of Laptop for Student ",self.name)
        #c = input("Which cpu is there in your Laptop ")  we can also use this to take user input for laptop configurations
        #r = input("How much RAM do you have?? ")
        self.lap = self.Laptop('i9',16)  # Creating an object of laptop for corresponding student

    def show(self):
        print("Student name is ",self.name)
        print("Student has laptop with following config ")
        self.lap.config()

    class Laptop:
        def __init__(self,cpu,ram):
            self.cpu = cpu
            self.ram = ram

        def config(self):
            print("processor - {} and RAM - {}GB".format(self.cpu,self.ram))


s1 = Student('Chand')
s1.show()

print("Below output is from config method wrt student object")
s1.lap.config()  # Calling method of inner class

lap1 = Student.Laptop('i7',8) #Creating object of Inner class
print("Object of laptop without any object of Student")
lap1.config()