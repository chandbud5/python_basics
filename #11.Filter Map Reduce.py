"""
Filter - It takes function and iterable as parameters (Give all even numbers


Instead of using lamdas we can use this function
def evens(n):
        return n%2==0

MAP - Increment all values by 2
def inc(n):
    return n+2

Reduce -   Sum of all numbers in list
def sum(a,b):
    return a+b
"""

from functools import reduce

lst = [2,3,5,4,8,0,9,12,23,45,67,89,64]

fltr = list(filter(lambda n : n%2==0 , lst))
print(fltr)

map = list(map(lambda n : n+2, fltr))
print(map)

red = reduce(lambda a,b:a+b,map)
print(red)
