# Part 4 User definied function

#Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:
# BMI = (weight in Kg)/(Height in Meters)^2.
# Write python code which can accept the weight and height of a person and calculate his BMI.
# note: Make sure to use a function which accepts the height and weight values and returns the BMI value.

def BMI(a,b):

    b = b*b
    bm = a/b

    return bm  

a = float(input("Enter your weight in Kg"))
b = float(input("Enter your height in meters"))
print(BMI(a,b))