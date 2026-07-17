from Data import Data
class App:
    def printMenu():
        print('Enter ItemId : ')
        for k,v in Data.items.items():
            print(k,v["name"],v["price"])
    printMenu()