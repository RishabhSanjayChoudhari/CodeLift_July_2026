from Data import Data
class App:
    def printMenu():
        print('Enter ItemId : ')
        for k,v in Data.items.items():
            if v["quantity"]> 0 :
                print(k,v["name"],"- ₹",v["price"], v["quantity"])
    
    
    def printOrderBill():
        orderId = input('Enter your orderId: ')
        print("")
        print("=" * 50)
        print('OrderId: ' , orderId)
        print("-" * 50)
        fulltotal = 0
        for item in Data.orders[orderId]["cart"]:
            qnt = item['quantity']
            amount =  item['price']
            total = item['quantity']  * item['price']
            print(amount,'x', qnt,'=', total)
            fulltotal +=total
        print("-" * 50)
        print("Subtotal : ₹", fulltotal)

        code = Data.orders[orderId]["promotions"]

        if code in Data.promotions:
            discount = Data.promotions[code]["discount_value"]

            fulltotal = fulltotal - discount

            print("Coupon Applied :", code)
            print("Discount       : ₹", discount)
            print("-" * 50)
            print("Total After Discount : ₹", fulltotal)
            print("+GST                 : 18% ")
            print('Total After Taxes    :', (fulltotal*0.18)+fulltotal)
            

        print("=" * 50)

    printMenu()
    printOrderBill()
    
    
    
    
    
def printOrders():
    cart = []

    while True:
        App.printMenu()

        itemId = int(input("Enter Product ID: "))

        if itemId not in Data.items:
            print("Please enter a correct ID.")
            continue

        order_quantity = int(input("Enter Quantity: "))

        name = Data.items[itemId]["name"]
        
        if Data.items[itemId]["quantity"] < order_quantity:
             print(f"Only {Data.items[itemId]['quantity']} items available.")
             
        # quantityleft = Data.items[itemId]['quantity']
        Data.items[itemId]["quantity"] -= order_quantity
        
        if order_quantity<=Data.items[itemId]['quantity'] :
            cart.append({
                        "name": name,
                        "itemId": itemId,
                        "quantity": order_quantity
                    })
            


        choice = input("Do you want to add anything else (y/n): ").lower()

        if choice != "y":
            break

    print(cart)

printOrders()

