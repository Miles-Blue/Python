import random

def lottery():
    #accepts no arguments
    #generates seven random lottery numbers
    #assigns them to a list and outputs the list
    
    lottery_numbers = [0] * 7
    
    try:
        print("Generating lotto numbers...")
        for index in range(len(lottery_numbers)):
            lottery_numbers[index] = random.randint(0, 9)
            
        print("Your lotto numbers are:")
        for element in lottery_numbers:
            print(element)
    except Exception as err:
        print(err)
        
def rainfall():
    #accepts no arguments
    #prompts user for rainfall for specified month
    #outputs the total rainfall, average monthly rainfall,
    #and the months with the highest and lowest amounts
    
    #Establishes MONTHS and rainfall_list as lists
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    rainfall_list = []
    
    #Sets total_rainfall to a number
    total_rainfall = 0
    
    try: #Exception handling
        for index in range(len(MONTHS)): #Prompts user for input for each month
            month = MONTHS[index]
            month_rainfall = int(input((f"Enter the rainfall for {month}: ")))
            rainfall_list.append(month_rainfall) #adds input to a list
            total_rainfall += month_rainfall
        average_rainfall = float(total_rainfall) / float(len(rainfall_list))
        
        #Gets the lowest and highest rain from the rainfall_list
        least_rain = min(rainfall_list)
        most_rain = max(rainfall_list)
        
        #Gets the lowest and highest month from the rainfall_list and MONTHS
        least_month = rainfall_list.index(min(rainfall_list))
        most_month = rainfall_list.index(max(rainfall_list))
        
        #Outputs everything and formats it
        print()
        print(f"{MONTHS[least_month]} had the least rain with {least_rain} inch(es) of rain")
        print(f"{MONTHS[most_month]} had the most rain with {most_rain} inch(es) of rain")
        print(f"Total rain for the year: {total_rainfall} inches")
        print(f"Average rain per month: {average_rainfall:.2f} inches")
        
    except Exception as err: #Exception handling
        print(err)

def charge_accts():
    #accepts no arguments
    #reads charge_accounts.txt into a list
    #prompts user for an account number
    #compares it to the list and outputs accordingly
    
    accounts_list = []
    
    try:
        account_file = open('charge_accounts.txt', 'r')
        for line in account_file:
            line = line.rstrip('\n')
            accounts_list.append(line)
            
        while True:
            try:
                user_search = int(input("Enter an account number: "))
                #valid = 
            except:
                print("\nEnter a numeric number only\n")
        
    except Exception as err:
        print(err)