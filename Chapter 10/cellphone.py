class CellPhone:
    
    def __init__(self, manu, model, r_price):
        self.__manufacturer = manu
        self.__model = model
        self.__price = float(r_price)
    
    def __str__(self):
        return f"Your phone is a {self.__manufacturer} model {self.__model} that retails for ${self.__price}"
    
    def set_manufact(self, user_input):
        self.__manufacturer = user_input
        return f"Manufacturer updated to {self.__manufacturer}"
    
    def set_model(self, user_input):
        self.__model = user_input
        return "Model updated to {self.__model}" 
    
    def set_retail_price(self, user_input):
        self._price = float(user_input)
        return "Retail price updated to {self.__price}"
    
    def get_manufact(self):
        return self.__manufacturer
    
    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return self.__price