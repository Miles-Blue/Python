class Retail:
    
    def __init__(self, item, units, price):
        self.__item = item
        self.__units = units
        self.__price = price
    
    def __str__(self):
        return f"There are {self.__units} {self.__item}(s) in stock and they ${self.__price} per unit."
    
    def set_item(self, item):
        self.__item = item
    
    def set_units(self, units):
        self.__units = units
    
    def set_price(self, price):
        self.__price = price
    
    def get_item(self):
        return self.__item
    
    def get_units(self):
        return self.__units
    
    def get_price(self):
        return self.__price
    