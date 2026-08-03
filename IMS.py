from Data import Data

class App:
    def printMenu(self):
        print('\n--- Available Items ---')
        for k, v in Data.items.items():
            if v["quantity"] > 0 and v.get("is_active", True):
                print(f"ID: {k} ]  {v['name']} - ₹{v['price']} (Stock: {v['quantity']})")

    def discountAmount(self, discount, fullTotal):
        discountValue = 0
        if discount['type'] == 'percent':
            discountValue = fullTotal * (discount['discount_value'] / 100)
            # Safe checking for max discount cap
            max_cap = discount.get('maximum_purchase') or discount.get('max_discount')
            if max_cap and discountValue > max_cap:
                discountValue = max_cap
        elif discount['type'] == 'amount':
            discountValue = discount['discount_value']
        return discountValue

    def discountCalc(self, discount, fullTotal):
        discountValue = 0
        min_purchase = discount.get('minimum_purchase', 0)
        if min_purchase <= fullTotal:
            discountValue = self.discountAmount(discount, fullTotal)
            if fullTotal < discountValue:
                discountValue = fullTotal
        return discountValue

    def printOrderBill(self, orderId):
        print("\n" + "=" * 50)
        print('OrderId: ', orderId)
        print("-" * 50)
        fulltotal = 0
        
        for item in Data.orders[orderId]["cart"]:
            qnt = item['quantity']
            amount = item['price']
            name = Data.items[item['product_id']]["name"]
            total=amount*qnt
            print(f"{name} ₹{amount} x {qnt} = ₹{total}")
            fulltotal+=total 
        print("-" * 50)
        print("Subtotal : ₹", fulltotal)

        code = Data.orders[orderId].get("promotions", None)
        if code and code in Data.promotions:
            discount = Data.promotions[code]
            discountValue = self.discountCalc(discount, fulltotal)
            if discountValue > 0:
                fulltotal -= discountValue
                print(f"Coupon Applied ({code}) : -₹{discountValue}")
                print(f"Total After Discount : ₹{fulltotal}")
        elif code:
            print("Invalid Promo Code Applied!")

        gst = fulltotal * 0.18
        print("-" * 50)
        print(f"+GST (18%)           : ₹{gst:.2f}")
        print(f"Total After Taxes    : ₹{fulltotal + gst:.2f}")
        print("=" * 50)

    def takeOrder(self):
        cart = []
        while True:
            self.printMenu()
            try:
                itemId = int(input("\nEnter Product ID: "))
            except ValueError:
                print("Please enter a valid numeric ID.")
                continue

            if itemId not in Data.items:
                print("Please enter a correct ID.")
                continue

            try:
                order_quantity = int(input("Enter Quantity: "))
            except ValueError:
                print("Please enter a valid quantity.")
                continue

            available_qty = Data.items[itemId]["quantity"]
            if available_qty < order_quantity:
                print(f"Only {available_qty} items available.")
            else:
                productprice = Data.items[itemId]['price']
                Data.items[itemId]["quantity"] -= order_quantity
                
                # Update cart
                quantityAvailable = False
                for product in cart:
                    if product['product_id'] == itemId:
                        product['quantity'] += order_quantity
                        quantityAvailable = True
                        break
                if not quantityAvailable:
                    cart.append({"product_id": itemId, "quantity": order_quantity, "price": productprice})

            choice = input("Do you want to add anything else (y/n): ").lower()
            if choice == "n":
                if not cart:
                    print("Cart is empty! Cannot create order.")
                    return None

                promoChoice = input("Do you want to add PROMO (y/n): ").lower()
                
                # Handle empty orders dict safely
                orderID = max([int(k) for k in Data.orders.keys()], default=0) + 1
                
                if promoChoice in['y','yes']:
                    user_promo = input("Enter Promo Code: ").strip().upper()
                    cart_subtotal=sum(item['price']*item['quantity']for item in cart)
                    if user_promo in Data.promotions:
                        promo_data=Data.promotions[user_promo]
                        min_req=promo_data.get('minimum_purchase',0)
                        if cart_subtotal>=min_req:
                            print(f"Promo Code'{user_promo}'applied successfully!")
                            Data.orders[orderID] = {"cart": cart, 'promotions': user_promo}
                        else:
                            print(f"'{user_promo}'requires a minimum purchase of  ₹{min_req}.(your total is  ₹{cart_subtotal})")
                            Data.orders[orderID]={'cart':cart}
                    else:
                        print(f"Invalid promo code:'{user_promo}'Does n ot exist.")   
                        Data.orders[orderID] = {"cart": cart}
                else:
                    Data.orders[orderID] = {"cart": cart}
                return orderID

    def start(self):
        while True:
            orderId = self.takeOrder()
            if orderId:
                self.printOrderBill(orderId)
            
            cont = input("\nDo you want to take another order? (y/n): ").lower()
            if cont != 'y':
                print("Thank you! Exiting system.")
                break
def main():
    app = App()
    app.start()

if __name__ == "__main__":
    main()