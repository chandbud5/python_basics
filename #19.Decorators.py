def div(a,b):
    return a/b

# If we always want result to be >= 1 and we do not have access to this defined function then we use decorators

def smart_div(func):

    def inner(a,b):  # Creating function inside function
        if a<b:
            return func(b,a)
    return inner

newdiv = smart_div(div)     # Linking new function to our previous function
print(newdiv(2,4))