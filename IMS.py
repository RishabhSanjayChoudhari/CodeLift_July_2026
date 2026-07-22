from Data import Data
class App:
    def printMenu():
        print('Enter ItemId : ')
        for k,v in Data.items.items():
            print(k,v["name"],v["price"])
    printMenu()      
    print("===========Inventory Management System============")  
    def printOrderRecipt(orderId):
        order=Data.orders[str(orderId)]
        itemList=order["cart"]
        for item in itemList:
            productName=Data.items[item["product_id"]]["name"]
            itemTotal=item["price"]*item["quantity"]
            print(productName,'$',item["price"],'x',item['quantity'],'=','$',itemTotal)
    printOrderRecipt(102)
    