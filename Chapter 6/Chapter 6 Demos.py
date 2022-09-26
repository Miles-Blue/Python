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

#def write_video_times():
    #acceps no arguments
    #prompts user for number of videos
    #and length of each video
    #writes them into video_times.txt while looping for total videos




























































































































































































