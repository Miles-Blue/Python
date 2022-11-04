import pickle

def write_main():
    #accepts no arguments
    #opens the file info.dat for binary writing
    #it loops and calls save_data to prompt the user for information
    #to add user data to dictionary
    #and prompts the user to continue
    
    #prime the loop
    again = 'y'
    
    #open the filefor binary writing
    outfile = open('info.dat', 'wb')
    
    #loops to get date until the user wants to stop
    while again.lower() == 'y':
        #get and save data
        save_data(outfile)
        
        #prompt the user continue
        again = input('Enter more data: (y/n): ')
        
    #data entry finished, close the file
    outfile.close()

def read_main():
    
    end_of_file = False
    
    infile = open('info.dat', 'rb')
    
    while not end_of_file:
        try:
            person = pickle.load(infile)
            display_data(person)
        except EOFError:
            end_of_file = True
    
    infile.close()

def display_data(person):
    
    print('Name: ', person['name'])
    print('Age: ', person['age'])
    print('Weight: ', person['weight'])
    print()
    
def save_data(file):
    
    person = {}
    
    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))
    
    pickle.dump(person, file)