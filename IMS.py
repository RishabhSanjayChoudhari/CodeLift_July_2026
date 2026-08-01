from Data import Data
class App:
    def printMenu():
        print('Enter ItemId : ')
        for k,v in Data.items.items():
            if v["quantity"]> 0 and v["is_active"] :
                print(k,v["name"],"- ₹",v["price"], v["quantity"])
    
    
    def printOrderBill(orderId):
        print("")
        print("=" * 50)
        print('OrderId: ' , orderId)
        print("-" * 50)
        fulltotal = 0
        for item in Data.orders[orderId]["cart"]:
            qnt = item['quantity']
            amount =  item['price']
            total = item['quantity']  * item['price']
            print(item["name"], "-",amount,'x', qnt,'=', total)
            fulltotal +=total
        print("-" * 50)
        print("Subtotal : ₹", fulltotal)
        
        code = Data.orders[orderId].get("promotions",None)
        if code != None :
            discount = Data.promotions[code]["discount_value"]
            fulltotal = fulltotal - discount
            print("Coupon Applied :", code)
            print("Discount       : ₹", discount)
            
        print("-" * 50)
        print("Total After Discount : ₹", fulltotal)
        print("+GST                 : 18% ")
        print('Total After Taxes    :', (fulltotal*0.18)+fulltotal)
            

        print("=" * 50)

    # printMenu()
    # printOrderBill()   
    
    def takeOrder(self):
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
            else:
                quantityAvailable = False
                productprice = Data.items[itemId]["price"]

                Data.items[itemId]["quantity"] -= order_quantity

                for product in cart:
                    if product["product_id"] == itemId:
                        product["quantity"] += order_quantity
                        quantityAvailable = True
                        break

                if not quantityAvailable:
                    cart.append({
                        "product_id": itemId,
                        "quantity": order_quantity,
                        "price": productprice
                    })

    choice = input("Do you want to add anything else (y/n): ").lower()

    if choice == "n":
        promoChoice = input("Do you want to add PROMO (y/n): ").lower()
        orderID = max(Data.orders) + 1

        if promoChoice == "y":
            promoCode = self.applycoupon(cart)

            if promoCode:
                Data.orders[orderID] = {
                    "cart": cart,
                    "promotions": promoCode
                }
            else:
                Data.orders[orderID] = {
                    "cart": cart
                }
        else:
            Data.orders[orderID] = {
                "cart": cart
            }
        return orderID
            
    def applycoupon(self, cart):
        promoCode = input("Enter Promo Code: ")

        if self.promoValidation(cart, promoCode):
            print("Coupon Applied Successfully")
            return promoCode

        return None

    def promoValidation(self, cart, promotions):
        fulltotal = 0
        promoValidation = False
        for item in cart:
            total = item['quantity'] * item['price']
            fulltotal += total
        if promotions in Data.promotions:
            if Data.promotions[promotions]['minimum_purchase'] <= fulltotal:
                promoValidation = True
        return promoValidation
                
                
    def start(self):
        while(True):
            orderId = self.takeOrder()
            self.printOrderBill(orderId)
            
    def main():
        app = App()
        app.start()

    if __name__ == "__main__":
        main()
