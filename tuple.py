'''
name:nicole nelson
python program
'''
inventory=[
    ("laptop",5,30000.00),
    ("headphones",15,500.0),
    ("mouse",5,250.0),
    ("keyboard",6,1500.0),
    ("monitor",6,2500)
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,price=item
    stock_value=quantity*price
    print(f"item_name:{item_name},the stock value is :{stock_value}")
    if stock_value>highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item_name
print(f"highest stock value is:{highest_stock_value}")
print(f"item with highest stock value is:{item_with_highest_stock_value}")
