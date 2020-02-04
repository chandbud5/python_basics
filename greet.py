# This file is used with #20.Special__name__.py



# Here we are setting a condition that when user will run this as main nodule then only print "Hello User"
# Otherwise it will not print if it is imported to another module
# TO verify run this and then run special__name__

if __name__=="__main__":
    print("Hello User")

print("Welcome User")
print("This name is from greet __name__ = ",__name__)