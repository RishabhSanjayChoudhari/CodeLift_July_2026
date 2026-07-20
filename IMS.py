from Data import Data
class App:
    def printMenu():
        print('Enter ItemId : ')
        for k,v in Data.items.items():
            print(k,v["name"],v["price"])
    printMenu()        
    def printRecipt():
        print('Enter Order id')
        order_id = str(input())
        for k,v in Data.orders.items():
            if k == order_id:
                print('ProductId','Quantity   X'   ,'Price')

                for i in v['cart']:
                    print(i['product_id'],i['quantity'],'X',i['price'])
                    print(' Total Price :',sum(i['price'] for i in v['cart']))
    printRecipt()                