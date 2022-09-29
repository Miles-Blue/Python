def line_numbers():
    #accepts no arguments
    #prompts user for file name
    #opens file and outputs each line
    #with increasing numbering
    
    counter = 0
    
    filename = input("Enter the file you wish to read: ")
    
    try: #error checking
        file_lines = open(filename, 'r')
        for line in file_lines:
            counter += 1
            print(counter, ": ", line, sep='')
    except FileNotFoundError:
        print("ERROR: File not found.")
    finally:
        file_lines.close()
            
#----------------------------------------------------------------------#
        
def line_counter():
    #accepts no arguments
    #prompts user for name of a file
    #program outputs total number of lines
    
    total = 0
    
    filename = input("Enter the file you wish to read: ")
    
    try: #error checking
        file_lines = open(filename, 'r')
        for line in file_lines:
            total += 1
        print(filename, "contains", total, "lines.")
    except FileNotFoundError:
        print("ERROR: File not found.")
    finally:
        file_lines.close()








































