from enum import Enum

class Unit(Enum):
    KG = 1
    LTR = 2
    PIECES = 3
    
class Data:
    items = {
        1: {
            "name": "milk",
            "price": 100,
            "quantity": 50,
            "unit": Unit.LTR,
            "is_active": True,
        },
        2: {
            "name": "sugar",
            "price": 50,
            "quantity": 100,
            "unit": Unit.KG,
            "is_active": True,
        },
        3: {
            "name": "Parle-G",
            "price": 5,
            "quantity": 1000,
            "unit": Unit.PIECES,
            "is_active": True,
        },
        4: {
            "name": "KrackJack",
            "price": 10,
            "quantity": 1000,
            "unit": Unit.PIECES,
            "is_active": True
        }
    }

    promotions = {
        "SUPER10": {
            "discount_type": "percent_off",
            "minimum_purchase": 500,
            "maximum_purchase": 1000,
            "discount_value": 20,
            "is_active": True,
        },
        "10SUPER": {
            "discount_type": "amount_off",
            "minimum_purchase": 1000,
            "maximum_purchase": 2000,
            "discount_value": 100,
            "is_active": True,
        },
    }

    orders = {
        "101": {
            "cart": [
                {"product_id": 1, "quantity": 20, "price": 200},
                {"product_id": 2, "quantity": 10, "price": 100},
                {"product_id": 3, "quantity": 200, "price": 1000},
            ]
        },
        "102": {
            "cart": [
                {"product_id": 1, "quantity": 20, "price": 200},
                {"product_id": 2, "quantity": 10, "price": 100},
                {"product_id": 3, "quantity": 200, "price": 1000},
            ]
        }
    }