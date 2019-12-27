#part 5 Exception handling

#Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception.
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Exception can't divide by zero"

a = int(input("Enter a number"))
b = int(input("Enter another number"))
print(divide(a,b))