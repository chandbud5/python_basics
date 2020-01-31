from array import *

x = array('i',[2,3,4,5,6,7,8,0])
print(x)

from numpy import *
# 6 Ways to create an array using Numpy

a = array([2,3,4,5]) # 1)array()
print(a)

b = linspace(1,15,15) # 2)linspace(start,stop,parts)
print(b)

c = logspace(1,40) # 3)logspace by default 50 parts will be created
print(c)

d = arange(0,10,2) #4)arange() it will be excluding the upper limit
print(d)

e = zeros(4)
print(e)

f = ones(4)
print(f)

#Copying Arrays : 1) Shallow copy (changes in one will reflect in another)
#                 2) Deep Copy (changes in one won't reflect in another)

#Shallow copy
shallow = a.view()
print("id of a is ",id(a))
print("id of shallow is ",id(shallow))
shallow[2] = 12
print(a)
print(shallow)

#Deep Copy
deep = a.copy()
print("id of a is ",id(a))
print("id of deep is ",id(deep))
deep[2] = 16
print(a)
print(deep)