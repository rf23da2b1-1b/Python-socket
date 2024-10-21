from RestClient import *

print(' Alle pizzaer')
pizzaer, resp = GetAll()
print(resp.status_code)
for p in pizzaer:
    print(p)

print('opret pizza')
nyPizza = { 'id':0, 'name': 'hawaii', 'description': 'det er go', 'price':54 }
resp = Add(nyPizza)
print(resp.status_code)
print(str(resp.content))

print(' Alle pizzaer igen ')
pizzaer, resp = GetAll()
print(resp.status_code)
for p in pizzaer:
    print(p)



