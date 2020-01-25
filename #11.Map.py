"""
Consider a list in Python which includes prices of all the items in a store.
Build a function to discount the price of all the products by 10%.
Use map to apply the function to all the elements of the list so that all the product prices are discounted.
"""

prices = [100,120,350,240,700,560]
"""
def discount(x):
    return x*0.9

result = list(map(discount,prices))
"""
result = list(map(lambda x : 0.9*x , prices))
print(result)