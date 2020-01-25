#create Dictionary with atleast five entries init
#Write code which accepts name of a product and in turn returns their respective prices.

laptop = {"Lenovo" : 40000, "Hp" : 55000, "Dell" : 50000, "Acer":35000 , "Apple":70000}

x = input("Enter company's name to get laptop price")
print("price of "+ x +"'s laptop is Rs. ")
print(laptop[x])