class Register:
    
    def __init__(self):
        self.__lst = []

    def purchase_item(self, item):
        self.__lst.append(item)
    
    def get_total(self):
        total = 0
        
        for item in self.__lst:
            total += item.get_price()
        
        return f"Your total is: ${total}"

    def show_cart(self):
        
        if len(self.__lst) == 0:
            return False
        
        else:
            for item in self.__lst:
                print(item)
                print()
            
            return True
        
    def empty(self):
        self.__lst.clear()
        
        print("\nCart successfully cleared!\n")
    
    def return_list(self):
        return self.__lst