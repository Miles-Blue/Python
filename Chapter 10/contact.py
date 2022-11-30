class Contact:
    
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email
    
    def __str__(self):
        return f"{self.__name} has the phone number of {self.__phone} and email of {self.__email}"
    
    def set_name(self, name):
        self.__name = name
        #return f"Name updated to {self.__name}"
        
    def set_phone(self, phone):
        self.__phone = phone
        #return f"Phone updated to {self.__phone}"
    
    def set_email(self, email):
        self.__email = email
        #return f"Email updated to {self.__email}"
        
    def get_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone
    
    def get_email(self):
        return self.__email