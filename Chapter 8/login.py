def get_login_name(first, last, idnumber):
    #accepts arguments for first, last, and idnumber
    #it creates separate substrings of the first 2 letters of both
    #the first name and the last name and the last 3 characters of idnumber
    #it concatenates the strings in the order of first, last, id
    #and returns the new enerated login
    
    new_login = first[0:3] + last[0:3] + idnumber[-3:]
    
    return new_login

def valid_password(password):
    #accepts a string for a password
    #it tests the following conditions
    #does the passowrd have at least one uppercase letter
    #does the password have at least on lowercase letter
    #does the password have at least on digit (numeric)
    #if the passowrd meets all conditions is_valid is true
    #valid_password returns is_valid
    
    is_valid = False
    counter = 0
    
    while not is_valid:
        counter += 1
        if counter >= 2:
            password = input("\nPlease enter your password: ")
        if not len(password) >= 7:
            print("\nThe password you entered is not valid. The password must be at least 7 characters long.")
            continue
        if password.isnumeric():
            print("\nThe password you entered is not valid. The password must contain at least one uppercase and one lowercase letter.")
            continue
        if password.islower():
            print("\nThe password you entered is not valid. The password must contain at least one uppercase letter.")
            continue
        if password.isupper():
            print("\nThe password you entered is not valid. The password must contain at least one lowercase letter.")
            continue        
        if password.isalpha():
            print("\nThe password you entered is not valid. The password must contain at least one digit(numeric).")
            continue
        is_valid = True
        
    print("\nPassword accepted")  
        
        
        
        
        