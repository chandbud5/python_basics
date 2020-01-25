#List out  all the odd numbers from 1 to 100 using lists in Python.

"""
l = []
for i in range(1,100):
    if(i%2==1):
        l.append(i)
"""

l = [x for x in range(100) if x%2==1]
print(l)