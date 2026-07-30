from Data import Data

class App:

    def printMenu():
        print("\nMain Menu")
        print("----------")
        for k, v in Data.items.items():
            if v["is_active"]:
                print(k, v["name"], v["price"], "Qty:", v["quantity"])

    def getValidYesNo(prompt):
        while True:
            answer = input(prompt).strip().lower()

            if answer in ("yes", "y"):
                return True

            if answer in ("no", "n"):
                return False

            print("Please enter yes or no.")

    def addItemsToCart():
        cart = []

        while True:
            App.printMenu()

            try:
                itemId = int(input("Enter Item Id: "))
            except ValueError:
                print("Invalid item id. Please enter a number.")
                continue

            item = Data.items.get(itemId)

            if not item:
                print("Item not found.")
                continue

            if not item["is_active"]:
                print("This item is not active and cannot be selected.")
                continue

            try:
                quantity = int(input("Enter Quantity: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                continue

            if quantity <= 0:
                print("Quantity out of range. Please enter a quantity greater than 0.")
                continue

            if quantity > item["quantity"]:
                print("Quantity not left. Quantity out of range for this item.")
                continue

            cart.append({
                "product_id": itemId,
                "quantity": quantity,
                "price": item["price"],
            })

            item["quantity"] -= quantity

            if not App.getValidYesNo("Do you want to add more items? yes/no: "):
                return cart

    def applyPromotion(total):

        discount = 0
        promoCode = None

        for code, promo in Data.promotions.items():

            if promo["is_active"]:

                if total >= promo["minimum_purchase"] and total <= promo["maximum_purchase"]:

                    promoCode = code

                    if promo["discount_type"] == "percent_off":
                        discount = total * promo["discount_value"] / 100

                    elif promo["discount_type"] == "amount_off":
                        discount = promo["discount_value"]

                    break

        return promoCode, discount


    def printOrderReceipt(orderId):

        order = Data.orders[orderId]
        itemList = order["cart"]

        total = 0

        for item in itemList:
            productName = Data.items[item["product_id"]]["name"]
            itemTotal = item["price"] * item["quantity"]
            total = total + itemTotal

            print(productName, "$", item["price"], "x", item["quantity"], "=", "$", itemTotal)

        print("----------------------------")
        print("Total :", total)

        promoCode, discount = App.applyPromotion(total)

        if promoCode:
            print("Promotion Applied :", promoCode)
            print("Discount :", discount)
            print("Final Total :", total - discount)
        else:
            print("No Promotion Applicable")


    def printReceiptFromCart(cart):
        total = 0

        for item in cart:
            productName = Data.items[item["product_id"]]["name"]
            itemTotal = item["price"] * item["quantity"]
            total = total + itemTotal

            print(productName, "$", item["price"], "x", item["quantity"], "=", "$", itemTotal)

        print("----------------------------")
        print("Total :", total)

        promoCode, discount = App.applyPromotion(total)

        if promoCode:
            print("Promotion Applied :", promoCode)
            print("Discount :", discount)
            print("Final Total :", total - discount)
        else:
            print("No Promotion Applicable")

    def start():
        cart = App.addItemsToCart()
        print("\nReceipt")
        print("--------")
        App.printReceiptFromCart(cart)


App.start()
