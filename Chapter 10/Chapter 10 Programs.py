import bankaccount 
import cellphone

def main():
    #accepts no arguments
    #takes input from the user for a starting balance
    #Uses the BankAccount class in bankaccount.py to create
    #an object savings, passing the starting balance
    #it takes input from the user for a paycheck
    #it displays the current balance using the get_balance() method
    #it takes input from the user for withdrawl and uses the withdraw() method
    #and outputs the final balance
    
    start_balance = float(input("Enter a starting balance: "))
    
    savings = bankaccount.BankAccount(start_balance)
    
    deposit_amount = float(input("Enter the amount of your paycheck to deposit: "))
    
    savings.deposit(deposit_amount)
    
    print(savings)
    
    withdraw_amount = float(input("Enter the amount you want to withdraw: "))
    
    savings.withdraw(withdraw_amount)
    
    print(savings)

def cell_phone():
    
    valid = False
    
    print("Welcome to the Galactic Phone Database.")
    
    manu = input("Enter the phone manufacturer: ")
    model = input("Enter the phone model number: ")
    
    while not valid:
        try:
            price = float(input(f"Enter the retail price for your {manu}, model {model}: "))
            valid = True
        except:
            valid = False
    
    info = cellphone.CellPhone(manu, model, price)
    
    print("\nHere is the data you entered:")
    print(f"Manufacturer: {info.get_manufact()}")
    print(f"Model: {info.get_model()}")
    print(f"Retail Price: ${info.get_retail_price()}")