import pickle
import cellphone

def main():
    make_list()


def make_list():
    
    file = open('cellphone_pickle.dat', 'wb')
    
    while True:
        valid = False
        
        manu = input("\nEnter the phone manufacturer: ")
        model = input("Enter the phone model: ")
        
        while not valid:
            try:
                price = float(input("Enter the retail price: "))
                valid = True
            except:
                valid = False
        
        info = cellphone.CellPhone(manu, model, price)
        
        pickle.dump(info, file)
        
        cont = input("\nEnter another phone? (y/n)")
        
        if cont.lower() == 'n':
            break
    
    file.close()
    print("\nAll data has been written to cellphone_pickle.dat")
    