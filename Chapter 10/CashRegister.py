class Register:
    
    def __init__(self):
        self.__lst = []

    def purchase_item(self, item):
        self.__lst.append(item)
    
    def get_total(self):
        total = 0
        
        for item in self.__lst:
            total += item.get_price()
        
        return total

    def show_cart(self):
        for item in self.__lst:
            print(item)
            print()
        
        if len(self.__lst) == 0:
            print("\nThere is nothing in your cart yet!\n")
    
    def empty(self):
        self.__lst.clear()
        
        print("\nCart successfully cleared!\n")
    