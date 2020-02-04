# Class B(A)------- Single Level Inheritance
# Class C(B).....Class B(A)--------Multi level inheritance
# Class C(B,A) -----Multiple inheritance
"""
Single Level Inheritance

class A:    #SuperClass
    def method1(self):
        print("Method 1 from Class A")

    def method2(self):
        print("Method 2 from Class A")

class B(A): # B is SubClass
    def method3(self):
        print("Method 3 from Class B")

    def method4(self):
        print("Method 4 from Class B")

obj = B()
obj.method1()
obj.method3()

Multi Level Inheritance

class A:
    def method1(self):
        print("Method 1 from Class A")

    def method2(self):
        print("Method 2 from Class A")

class B(A):
    def method3(self):
        print("Method 3 from Class B")

    def method4(self):
        print("Method 4 from Class B")

class C(B):
    def method5(self):
        print("Method 5 class C")

obj1 = C()
obj1.method1()
obj1.method3()
obj1.method5()

#Multi level inheritance

class A:
    def method1(self):
        print("Method 1 from Class A")

class B:
    def method1(self):
        print("Method 1 from Class B")

    def method2(self):
        print("Method 2 from class B")

class C(A,B):
    def method3(self):
        print("Method 3 from Class C")

obj1 = C()
obj1.method1()  # By default it will call method 1 of class A though class B also has method1--It will follow MRO(method resolution order)
obj1.method2()
"""

# Constructors in inheritance
class A:    #SuperClass

    def __init__(self):
        print("__init__ of class A")

    def method1(self):
        print("Method 1 from Class A")

    def method2(self):
        print("Method 2 from Class A")

class B(A):  #  B is SubClass

    def __init__(self):
        super().__init__()  #To call constructor(__init__) of super class
        print("__init__ of class B")

    def method3(self):
        print("Method 3 from Class B")

    def method4(self):
        print("Method 4 from Class B")

obj = B()