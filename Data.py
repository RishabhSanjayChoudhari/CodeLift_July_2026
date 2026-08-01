from enum import Enum

class Unit(Enum):
    KG = 1
    LTR = 2
    PIECES = 3
    
class Data:
    items = {
        1: {
            "name": "milk",
            "price": 50,
            "quantity": 500,
            "unit": Unit.LTR,
            "is_active": True,
        },
        2: {
            "name": "sugar",
            "price": 100,
            "quantity": 100,
            "unit": Unit.KG,
            "is_active": True,
        },
        3: {
            "name": "Parle-G",
            "price": 10,
            "quantity": 100,
            "unit": Unit.PIECES,
            "is_active": True,
        },
        4: {
            "name": "KrackJack",
            "price": 10,
            "quantity": 1000,
            "unit": Unit.PIECES,
            "is_active": True
        },

        5: {
            "name": "salt",
            "price": 20,
            "quantity": 100,
            "unit": Unit.KG,
            "is_active": True,
        },

        6: {
            "name": "cooking oil",
            "price": 150,
            "quantity": 100,
            "unit": Unit.LTR,
            "is_active": True,
        },

        7: {
            "name": "tea powder",
            "price": 250,
            "quantity": 80,
            "unit": Unit.KG,
            "is_active": True,
        },

        8: {
            "name": "coffee",
            "price": 450,
            "quantity": 50,
            "unit": Unit.KG,
            "is_active": True,
        },

        9: {
            "name": "Oats",
            "price": 180,
            "quantity": 75,
            "unit": Unit.KG,
            "is_active": True,
        },

        10: {
            "name": "Coca-Cola",
            "price": 75,
            "quantity": 100,
            "unit": Unit.LTR,
            "is_active": True,
        },

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
            "minimum_purchase":500,
            "maximum_purchase":1000,
            "discount_value": 200,
            "is_active": True,
        },
    }

    orders = {
        101: {
            "cart": [
                {"product_id": 1, "quantity": 5, "price": 50},
                {"product_id": 2, "quantity": 10, "price": 100},
                {"product_id": 3, "quantity": 200, "price": 10},
            ],
            "promotions": "10SUPER"
        },
        102: {
            "cart": [
                {"product_id": 1, "quantity": 20, "price": 50},
                {"product_id": 2, "quantity": 10, "price": 100},
                {"product_id": 4, "quantity": 150, "price": 10},
            ],
            "promotions": "SUPER10"
        }
    }