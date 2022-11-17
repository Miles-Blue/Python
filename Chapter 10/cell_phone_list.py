import cellphone

def main():
    phones = make_list()
    
    display_list(phones)

def make_list():
    
    phone_list = []
    
    for num in range(1, 5+1):
        valid = False
        
        manu = input(f"\nEnter the phone manufacturer for phone {num}: ")
        model = input(f"Enter the phone model number for phone {num}: ")
        
        while not valid:
            try:
                price = float(input(f"Enter the retail price for phone {num}: "))
                valid = True
            except:
                valid = False
        
        info = cellphone.CellPhone(manu, model, price)
        
        phone_list.append(info)
    
    return phone_list

def display_list(phone_list):
    
    counter = 0
    
    print("\nHere is the data you entered:")
    
    for phone in phone_list:
        counter += 1
        
        print(f"\nPhone #{counter}")
        print(f"\tManufacturer: {phone.get_manufact()}")
        print(f"\tModel: {phone.get_model()}")
        print(f"\tRetail Price: ${phone.get_retail_price()}")
