import os

def file_write():
    #accepts no arguments
    #opens file lotr.txt
    #and writes the names of three lotr characters
    
    outfile = open('lotr.txt', 'w')
    outfile.write('Spongebob\nPatrick\nSquidward')
    outfile.close()
    
def file_read():
    #accepts no arguments
    #opens file lotr.txt
    #and reads the entire contents of the file
    #then outputs the contents of the file
    
    infile = open('lotr.txt', 'r')
    
    print(infile.read())
    infile.close()

def line_read():
    #accepts no arguments
    #opes the file lotr.txt
    #reads the contents of the file one line at a time
    #outputs the contents of the file
    
    infile = open('lotr.txt', 'r')
    
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    infile.close()
    
    print(line1)
    print(line2)
    print(line3)
    
def append_names():
    #accepts no arguments
    #prompts the user for the names of three friends
    #and assigns each name to a unique variable
    #it opens friends.txt and writes each name to the file
    #on it's own line in the file
    
    print("Please enter the names of three friends")
    
    friend1 = input("Friend 1: ")
    friend2 = input("Friend 2: ")
    friend3 = input("Friend 3: ")
    
    outfile = open('friends.txt', 'a')
    outfile.write(friend1 + '\n')
    outfile.write(friend2 + '\n')
    outfile.write(friend3 + '\n')
    
    outfile.close()
    
def strip_newline():
    #accepts no arguments
    #opens the file lotr.txt and reads each line
    #strips the newline '\n' characters from each line
    #and prints the lines
    
    stripfile = open('lotr.txt', 'r')
    line1 = stripfile.readline()
    line2 = stripfile.readline()
    line3 = stripfile.readline()
    stripfile.close()
    
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    stripfile.close()
    
    print(line1)
    print(line2)
    print(line3)
    
def write_numbers():
    #accepts no arguments
    #takes inputs from the user in the form of three integers
    #opens the file numbers.txt
    #and writes the three numbers to the file as strings
    
    numfile = open('numbers.txt', 'w')
    
    num1 = input("Please enter a number: ")
    num2 = input("Please enter a number: ")
    num3 = input("Please enter a number: ")
    
    numfile.write(str(num1) + '\n')
    numfile.write(str(num2) + '\n')
    numfile.write(str(num3) + '\n')
    
    numfile.close()

    print("Your numbers have been written to numbers.txt.")

def read_numbers():
    #accepts no arguments
    #it opens the file numbers.txt and reads in each line
    #converting each from a string to an integer
    #it totals and outputs the three numbers and their total
    
    infile = open('numbers.txt', 'r')
    
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    
    infile.close()
    
    total = num1 + num2 + num3
    
    print("Here is your problem:", num1, "+", num2, "+", num3, "=", total)
    
def write_sales():
    #accepts no arguments
    #prompts the user for the number of days to input sales
    #for each iterations it writes the sale to the file sales.txt
    #after all days have been processed
    #it closes the file and outputs a message
    
    outfile = open('sales.txt', 'w')
    
    days = int(input("How many days do you want to enter sales for? "))
    
    for line in range(1, days + 1):
        sales = str(input("Enter the sales for day #" + str(line) + ": "))
        outfile.write(sales + '\n')
        
    outfile.close()
    print("All data has been saved to sales.txt.")
    
def read_sales():
    #accepts no arguments
    #opens and reads from sales.txt
    #loops until it reaches the end of the file
    #eac iterations of the loops will output the amount
    #and read the next line
    
    read_file = open('sales.txt', 'r')
    
    for line in read_file:
        number = float(line)
        print(number)
    read_file.close()

def write_video_times():
    #acceps no arguments
    #prompts user for number of videos
    #and length of each video
    #writes them into video_times.txt while looping for total videos
    
    num_vid = int(input("How many videos are in the project? "))
    
    videofile = open('video_times.txt', 'w')
    
    for video in range(1, num_vid+1):
        time = input("How long is video #" + str(video) + "? ")
        videofile.write(time + "\n")
    
    videofile.close()
    print("All times have been written.")
    
def read_video_times():
    #accepts no arguments
    #opens video_times.txt
    #loops for each line in video_times.txt
    #outputs total time for all videos
    
    videofile = open('video_times.txt', 'r')
    
    total = 0.0
    counter = 0
    
    for video in videofile:
        counter += 1
        time = float(video.rstrip('\n'))
        print("Video #" + str(counter) + " time is " + str(time) + " secs")
        total += time
        
    videofile.close()
    print("The total time for all the videos is", total, "secs.")
    
def save_emp_records():
    #accepts no arguments
    #prompts the user for the number of employee records
    #opens a file employees.txt and saves
    #the records Name, ID #, and Department to the file
    #it outputs a finished message with the filename
    
    total_records = int(input("How many employee records do you want to enter? "))
    while total_records < 0:
        total_records = int(input("Please enter more than 0 records. "))
        
    recordfile = open('employees.txt', 'w')
    
    for record in range(1, total_records+1):
        print("\nEnter data for employee #" + str(record))
        name = input("Name: ")
        id_num = input("ID Number: ")
        department = input("Department: ")
        recordfile.write(name + '\n' + id_num + '\n' + department + '\n')
    recordfile.close()
    print("All records were saved to employees.txt.")

def read_emp_records():
    #accepts no arguments
    #opens the file employees.txt
    #and loops for each line in the file
    #outputting the record for Employee Name, ID#, and Dept
    
    recordfile = open('employees.txt', 'r')
    
    counter = 0
    
    for line in recordfile:
        counter += 1
        
        name = line
        id_num = recordfile.readline()
        department = recordfile.readline()
        
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        department = department.rstrip('\n')
        
        print("\nRecord for employee #" + str(counter))
        print("Name:", name)
        print("ID Number:", id_num)
        print("Department:", department)
        
    recordfile.close()
    print("")
    print(counter, "records retrieved.")

#----------------------------------------------------#
def write_coffee():
    #accepts no arguments
    #opens the file coffe.txt to append
    #it loops while the user wants to continue entering records
    #prompts the user for the coffee description and number of pounds
    #the user should be prompted if they want to continue
    
    #prim the loop, open the file to append, display the header
    another = 'y'
    coffee_file = open('coffee.txt', 'a')
    
    #loop to get the records
    while another.lower() == 'y':
        print("Enter the following coffee data:\n")
        desc  = input("Description: ")
        pounds = input("Quantity (in pounds): ")
        
        #append the data to the file
        coffee_file.write(desc + '\n')
        coffee_file.write(pounds + '\n')
        
        #prompt for another entry
        another = input("\nDo you wish to enter another coffee? (y to continue): ")
        
    #close the file and output saved message
    coffee_file.close()
    print("\nAll data appended to coffee.txt.")
    
def read_coffee():
    #accepts no arguments
    #loops to read the record in coffee.txt
    #and outputs the description and pounds of coffee
    
    #open coffee.txt and read the first description
    coffee_file = open('coffee.txt', 'r')
    desc = coffee_file.readline()
    
    #loop to read, strip, and output each record
    while desc != '':
        pounds = coffee_file.readline()
        
        #strip the newline
        desc = desc.rstrip('\n')
        pounds = pounds.rstrip('\n')
        
        print("\nDescription:", desc)
        print("Quantity (in pounds):", pounds)
        
        #get the new description
        desc = coffee_file.readline()
        
    #close the file and output to the user
    coffee_file.close()
    print("\nAll records retrieved.")

def search_coffee():
    #accepts no arguments
    #searches coffee.txt for a string the user enters
    #if no record matches, it outputs a message to the user
    
    #boolean flag to determine search status
    found = False
    
    #get input from the user
    search = input("Enter a coffee descriptions to search for: ")
    
    #open the file coffee.txt
    coffee_file = open('coffee.txt', 'r')
    
    #get the first descriptions from the file
    desc = coffee_file.readline()
    
    #loop to read each line of the file
    while desc != '':
        pounds = coffee_file.readline()
        
        #strip the newline from the description
        desc = desc.rstrip('\n')
        
        if desc.lower() == search.lower(): #determine if the record is found and display the record
            print("\nRecord found!\n")
            print("Description:", desc)
            print("Quantity (in pounds):", pounds)
            found = True #toggle the flag variable to true
            
        #get the next description
        desc = coffee_file.readline()
        
    coffee_file.close()
    
    if not found: #found = false
        print("\nThe record was not found.")

def modify_coffee():
    #accepts no arguments
    #imports os module - this is needed to perform OS related file commands
    #searches through the records and allows the user to modify the quantity
    
    #boolean flag variable
    found = False
    
    #Get the search description and new quantity
    search = input("Enter the coffee description to modify: ")
    new_qty = input("Enter the new quantity: ")
    
    #open the coffee.txt file to read and a new temporary file to write
    coffee_file = open('coffee.txt', 'r')
    temp_file = open('temp.txt', 'w')
    
    #read the first description
    desc = coffee_file.readline()
    
    #loop to read and process each line
    while desc != '':
        qty = coffee_file.readline()
        
        #strip newline
        desc = desc.rstrip('\n')
        qty = qty.rstrip('\n')
        
        if search.lower() == desc.lower(): #coffee found
            #write the description and new quantity to the temp file
            temp_file.write(desc + '\n')
            temp_file.write(new_qty + '\n')
            found = True
        else: #these are not the droids you're looking for
            #write the original record to the temp file
            temp_file.write(desc + '\n')
            temp_file.write(qty + '\n')
        
        #read the next description
        desc = coffee_file.readline()
            
    #all records have been processed, remove and rename files
    coffee_file.close()
    temp_file.close()
        
    #delete the original
    os.remove('coffee.txt')
        
    #rename the temp file to coffee.txt
    os.rename('temp.txt', 'coffee.txt')
        
    #description not found
    if found == False:
        print("\nRecord not found.")
    else:
        print("The quantity for", search, "has been updated to", new_qty, "pounds.")

def delete_coffee():
    #accept no arguments
    #imports os module - this is needed to perform OS related file commands
    #searches through the records and allows the user to modify the quantity
    
    #boolean flag variable
    found = False
    
    #Get the search description and new quantity
    search = input("Enter the coffee description to delete: ")
    
    #open the coffee.txt file to read and a new temporary file to write
    coffee_file = open('coffee.txt', 'r')
    temp_file = open('temp.txt', 'w')
    
    #read the first description
    desc = coffee_file.readline()
    
    #loop to read and process each line
    while desc != '':
        qty = coffee_file.readline()
        
        #strip newline
        desc = desc.rstrip('\n')
        qty = qty.rstrip('\n')
        
        if search.lower() != desc.lower(): #coffee found
            #Deletes the description and qty of coffee
            temp_file.write(desc + '\n')
            temp_file.write(qty + '\n')
        else:
            #write the original record to the temp file
            found = True
        
        #read the next description
        desc = coffee_file.readline()
            
    #all records have been processed, remove and rename files
    coffee_file.close()
    temp_file.close()
        
    #delete the original
    os.remove('coffee.txt')
        
    #rename the temp file to coffee.txt
    os.rename('temp.txt', 'coffee.txt')
        
    #description not found
    if found == False:
        print("\nRecord not found.")
    else:
        print("The coffee record for", desc, "has been removed.")

def coffee_shop():
    #accepts no arguments
    #it calls coffee_shop_menu to display a menu to the user
    #and calls each function according to the user input
    
    option = 0
    while option != 5:
        option = coffee_shop_menu()
        if option == 1:
            write_coffee()
        elif option == 2:
            modify_coffee()
        elif option == 3:
            delete_coffee()
        elif option == 4:
            read_coffee()
        else:
            print()
    print("Thank you for using our program!")

def coffee_shop_menu():
    #accepts no arguments
    #displays the menu and prompts user for an option
    #returns the user option
    
    print("\nWelcome to Caffeine Overload Inventory Control System. Please choose an inventory option:")
    print("1) Add a record")
    print("2) Modify a record")
    print("3) Delete a record")
    print("4) Display all records")
    print("5) Exit")
    
    try:
        option = int(input("Inventory option: "))
        while not option >= 1 and not option <= 5:
            option = int(input("Please enter a valid option 1-5: "))
    except:
        print("That is not a valid option")
    return option
#----------------------------------------------------#

def division():
    #accepts no arguments
    #prompts the user for two integers
    #divides num1 / num2 and outputs the result
    
    #flag variable
    error = True
    
    #get input from the user
    while error: #error checks for alpha keys
        try:
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter a second number: "))
            while num2 == 0: #checks for divide by zero
                num2 = int(input("\nPlease enter a number other than 0 for second number: "))
            error = False
        except:
            print("\nEnter numbers only please.\n")
                   
    #perform calculations and output
    result = num1 / num2
    
    print("\n", num1, "divided by", num2, "is", result)
    
    
def gross_pay1():
    #accepts no arguments
    #prompts user for hours worked and pay rate
    #multiplies for gross pay
    
    #flag variable
    error = True
    
    while error: #validates answer for it being a float
        try:
            hours = float(input("Enter the number of hours worked: "))
            rate = float(input("Enter the pay rate: "))
            error = False
        except ValueError:
            print("ERROR: Please enter numbers only.\n")
            
    pay = hours * rate
    print("\nGross pay: $", format(pay, '.2f'), sep='')
    
def display_file1():
    #accepts no arguments
    #takes input from the user for a filename to open
    #and reads the contents of the file
    
    try: #exception for file so it does not crash
        #get input from the user
        filename = input("Enter filename to open: ")
            
        #open the file and read the contents
        infile = open(filename, 'r')
        contents = infile.read()
        
        #output and close the file
        print('\n' + contents)
        infile.close()
    except FileNotFoundError:
        print("Could not find file. Please enter a valid file.")
    
def sales_report1():
    #accepts no arguments
    #opens a file sales_data.txt to read
    #it accumulates the total for each line in the file
    
    total = 0
    
    try:
        infile = open('sales_data.txt', 'r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
    except IOError:
        print("ERROR: An error occured trying to read the file.")
    except ValueError:
        print("ERROR: Non-numeric data found, calculations haulted.")
    except:
        print("ERROR: A problem was encountered.")
    else:
        print(format(total, '.2f'))
    
    
    
    
    
    
    
    
    
    
    
    
    