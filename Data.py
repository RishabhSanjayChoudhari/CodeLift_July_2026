from enum import Enum

class Unit(Enum):
    KG = 1
    LTR = 2
    PIECES = 3
    
class Data:
    items = {
        1: {
            "name": "COW MILK",
            "price": 50,
            "quantity": 50,
            "unit": Unit.LTR,
            "is_active": True,
        },
        2: {
            "name": "SUGAR",
            "price": 50,
            "quantity": 50,
            "unit": Unit.KG,
            "is_active": True,
        },
        3: {
            "name": "PARLE-G",
            "price": 10,
            "quantity": 1000,
            "unit": Unit.PIECES,
            "is_active": True,
        },
        4: {
            "name": "KRACKJACK",
            "price": 10,
            "quantity": 1000,
            "unit": Unit.PIECES,
            "is_active": True
        }
    }

    promotions = {
        "SUPER10": {
            "type": "percent",
            "minimum_purchase": 500,
            "maximum_purchase": 1000,
            "discount_value": 20,
            "is_active": True,
        },
        "10SUPER": {
            "type": "amount",
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
                ],
            "promo_code": "SUPER10",
        },
        "102": {
            "cart": [
                {"product_id": 1, "quantity": 20, "price": 200},
                {"product_id": 2, "quantity": 10, "price": 100},
                {"product_id": 3, "quantity": 200, "price": 1000},
            ],
        }
    }