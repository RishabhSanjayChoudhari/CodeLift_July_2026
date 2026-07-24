from Data import Data
class App:
    def printMenu():
        print('Enter ItemId : ')
        for k,v in Data.items.items():
            if v["is_active"]==True and v["quantity"]>=1:
                print(k,v["name"],v["price"])
            
    # printMenu() 
         
    print("===========Inventory Management System============")  
    def printOrderRecipt(orderId):
        print("-"*50)
        order=Data.orders[str(orderId)] 
        itemList=order["cart"]
        promo=order["promo_code"]
        print(promo)
            
        for item in itemList:
                productName=Data.items[item["product_id"]]["name"]
                itemTotal=item["price"]*item["quantity"]
                print(productName,'$',item["price"],'x',item['quantity'],'=','$',itemTotal)
        print(promo,'Applied')
        Discount=itemTotal*0.2
        FinalAmmount=itemTotal-Discount
        print("Discount=",Discount)
        print("FinalAmount=",FinalAmmount)
            
          
    printOrderRecipt(101)
    print("-"*50)
    
    
    
