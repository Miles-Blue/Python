import pickle

def main():
    file = open('cellphone_pickle.dat', 'rb')
    
    while True:
        try:
            phone = pickle.load(file)
            
            display_data(phone)
            
            print()
            
        except EOFError:
            break
        
        except Exception as err:
            print(err)
            break
    
    file.close()
    
def display_data(phone):
    
    print(f"Manufacturer: {phone.get_manufact()}")
    print(f"Model: {phone.get_model()}")
    print(f"Retail Price: ${phone.get_retail_price()}")