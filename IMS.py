from Data import Data
class App:
    def printMenu():
        print('Enter ItemId : ')
        for k,v in Data.items.items():
            if v["is_active"]==True and v["quantity"]>=1:
                print(k,v["name"],v["price"])
            
    printMenu() 
    print("-"*50)                                    
    print("***********Inventory Management System***********")  
    def printOrderRecipt(orderId):
        print("="*50)
        order=Data.orders[str(orderId)] 
        itemList=order["cart"]
        promo=order["promo_code"]
        print(promo)
        subtotal=0
        for item in itemList:
                productName=Data.items[item["product_id"]]["name"]
                itemTotal=item["price"]*item["quantity"]
                subtotal +=itemTotal
                print(productName,'₹',item["price"],'x',item['quantity'],'=','₹',itemTotal)
        print("-"*50)        
        
        print("TAX")
        gst=subtotal*0.18
        Ammount_with_gst=subtotal+gst
        
        print("Subtotal :",subtotal)
        print("GST :(18%)",gst)
        print("Amount with GST:",Ammount_with_gst)
        print("-"*50)
       
        
        print(promo,'Applied')
        Discount=Ammount_with_gst*0.2
        Ammount_after_discount=Ammount_with_gst-Discount
        print("Discount=",Discount)
        print("FinalAmount=",Ammount_after_discount)
            
     

    print("-"*50)
   #take order item id quanitity
    def order():
      cart =[]
      while True:
       product_id=input("Enter Product Id")
       quantity=input("Enter quantity")
       price=Data.items[int(product_id)]["price"]
       cart.append({
           "product_id":int(product_id),
           "price":price,
           "quantity":int(quantity)})
       choice=input("Add Another item?(yes/no):")
       if choice.lower()=="no":
          break
       Data.orders["103"]={ "cart": cart,
                        "promo_code":"SUPER10"} 
    
    order()
    print("-"*50)
    printOrderRecipt("103")
     