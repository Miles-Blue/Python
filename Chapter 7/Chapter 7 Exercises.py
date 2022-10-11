import random

def lottery():
    #accepts no arguments
    #generates seven random lottery numbers
    #assigns them to a list and outputs the list
    
    lottery_numbers = [0, 0, 0, 0, 0, 0, 0]
    
    print("Generating lotto numbers...")
    for index in range(len(lottery_numbers)):
        lottery_numbers[index] = random.randint(0, 9)
        
    print("Your lotto numbers are:")
    for element in lottery_numbers:
        print(element)