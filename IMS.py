from Data import Data
class App:
    def printMenu():
        print('Enter ItemId : ')
        for k,v in Data.items.items():
            print(k,v["name"],v["price"])
    
    
    def printOrder():
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

    #PrintMenu
    printMenu()
    
    printOrder()
