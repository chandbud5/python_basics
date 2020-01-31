# Keyword length argument

def info(name, **details):
    print("Name is "+name)
    for i,j in details.items():
        print(i,j)

info('Chand', age=18, city='Rajkot',field='CSE')
