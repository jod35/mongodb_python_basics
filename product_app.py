from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017')

db=client['shop']


products=db.products
print(products)

print("Welcome to the product App!")
name=input("enter enter product name: ")
stock=input(("enter enter product stock: "))
cost_price=int(input("enter enter product cost_price: "))
markup=int(input("enter enter product markup: "))
discount=int(input("enter enter product discount: "))

disc= discount/100
makup=cost_price*(markup/100)
sell_price=cost_price+makup
gross_price=sell_price-disc

product_info= {}
product_info['name']=name
product_info['cost_price']=cost_price
product_info['stock']=stock
product_info['cost_price']=cost_price
product_info['markup']=markup
product_info['selling_price']=gross_price

print(product_info)

products_list=[]

res=products.insert_one(product_info)

if res.acknowledged:
    print("New document with ID %s has been created successfully"%res.inserted_id)

