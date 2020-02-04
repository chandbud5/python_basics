# Operator Overloading

# We need to perform addition on our class Student that add the marks of 2 student
# '+' is defined for int,str and other inbuilt classes but not for student
# So we will overload '+' operator for Student class
"""
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

# Operator Overloading
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s = Student(m1,m2)
        return s

# Method Overloading - Python directly does not support method overloading so we have created this indirectly
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a


s1 = Student(60,45)
s2 = Student(78,89)

s3 = s1+s2

print(s3.m1,s3.m2)
print(s1.sum(32,98,12))
"""

# Method Overriding - 2 methods with same name and same number of parameters but they are in different class

class A:
    def show(self):
        print("In A Show")

class B(A):
    def show(self):
        print("In B Show")

obj = B()
obj.show()  # If we do not have show in B then it will call show of A but if we have show in both then
            # show of B will override show of A