# global variables
a = 10
b = 12

"""
def function():

    #a = 5  # Local Variable
    global a
    a = 18  # Global variable
    print("Local a is ",a)

print("Global a is ",a)
function()
"""
"""
def func1():

    a = 5
    print("Local a is ",a)
    globals()['a']= 9 # global variable
    

func1()
print("Global a is ", a)
"""