from Data import Data

class App:

    def printMenu():
        print('Enter ItemId : ')
        for k, v in Data.items.items():
            print(k, v["name"], v["price"])

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


App.printOrderReceipt(102)
