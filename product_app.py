from pymongo import MongoClient
from pprint import pprint
client=MongoClient('mongodb://localhost:27017')

db=client['shop']


products=db.products
# print(products)

def create_product():
    print("Add a product!")
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

   

    products_list=[]

    res=products.insert_one(product_info)

    if res.acknowledged:
        print("New document with ID %s has been created successfully"%res.inserted_id)

def retrieve_products():
    all_products=products.find()
    for product in all_products:
        pprint(product)
        print('\n')

def conditionn_search():
    name=input("enter the name of the product: ")
    one_product=products.find({'name':name})
    for o in one_product:
        if o :
            pprint(o)
        else:
            print("No document with such name")

def sort_products():
    all_products=products.find().sort('name',1) #ascending order
    for product in all_products:
        pprint(product)
        print('\n')



while True:
    print("Welcome to the Product App!!\n1.Add A product\n2.View all products\n3.Search according to name\n4.Sort Items\n0.Exit")
    choice=int(input("ENTER YOU CHOICE: "))
    if choice ==1:
        create_product()
    elif choice ==2:
        retrieve_products()
    elif choice ==3:
        conditionn_search()
    elif choice ==4:
        sort_products()
    elif choice ==0:
        break
    else:
        print('Invalid input!!!!!')
        


