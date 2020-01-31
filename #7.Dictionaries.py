
#create Dictionary with atleast five entries init
#Write code which accepts name of a product and in turn returns their respective prices.

laptop = {"Lenovo" : 40000, "Hp" : 55000, "Dell" : 50000, "Acer":35000 , "Apple":70000}

x = input("Enter company's name to get laptop price")
print("price of "+ x +"'s laptop is Rs. ")

# To get value by using key and if not found then print message
print(laptop.get(x,"NOT FOUND"))

# TO add data in dictionaries
laptop["Asus"] = 38000

print(laptop)



# to make a dictionary using two list
key = [1,2,3]
vals = ['A','B','C']
dictionary = dict(zip(key,vals))

print(dictionary)



# Dictionary with lists and dictionary
ide = {'C#':'Visual Studio','Python':['PyCharm','Subime'],'Java':{'SE':'Netbeans','EE':'Eclipse'}}
# To fetch values
print(ide['C#'])
print(ide['Python'][0])
print(ide['Java']['SE'])