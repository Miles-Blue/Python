def encode():
    #accepts no arguments
    #opens file plaintext.txt and encodes each letter
    #using the dictionary
    #then prints it all to encoded.txt
    
    code = {'A' : '!', 'a' : '@', 'B' : '#', 'b' : '$', 'C' : '%', 'c' : '^', 'D' : '&', 'd' : '*',
            'E' : '(', 'e' : ')', 'F' : '1', 'f' : '2', 'G' : '3', 'g' : '4', 'H' : '5', 'h' : '6',
            'I' : '7', 'i' : '8', 'J' : '9', 'j' : '0', 'K' : '-', 'k' : '_', 'L' : '+', 'l' : '=',
            'M' : '<', 'm' : ',', 'N' : '>', 'n' : '.', 'O' : '?', 'o' : '/', 'P' : ':', 'p' : ';',
            'Q' : '{', 'q' : '}', 'R' : '[', 'r' : ']', 'S' : '~', 's' : '`', 'T' : 'Á', 't' : 'á',
            'U' : '§', 'u' : 'ß', 'V' : 'Ú', 'v' : 'ú', 'W' : 'Ä', 'w' : 'ä', 'X' : 'Ö', 'x' : 'ö',
            'Y' : 'Ø', 'y' : 'ø', 'Z' : 'Ñ', 'z' : 'ñ'}
    
    #Exception handling
    try:
        #Opens the files
        original = open('plaintext.txt', 'r')
        encoded = open('encoded.txt', 'w')
        
    except Exception as err: #Error handling
        print(err)
    
    #Replaces each letter with its encoded counterpart
    for line in original:
        line = line.rstrip('\n')
        for letter in line:
            if letter in code:
                line = line.replace(letter, code[letter])
        
        #Writes the new line to encoded.txt
        encoded.write(line + '\n')
    
    #Closes the files
    original.close()
    encoded.close()
    
def decode():
    #accepts no arguments
    #opens encoded.txt and decodes its message
    #then outputs the message in english
    
    code = {'A' : '!', 'a' : '@', 'B' : '#', 'b' : '$', 'C' : '%', 'c' : '^', 'D' : '&', 'd' : '*',
        'E' : '(', 'e' : ')', 'F' : '1', 'f' : '2', 'G' : '3', 'g' : '4', 'H' : '5', 'h' : '6',
        'I' : '7', 'i' : '8', 'J' : '9', 'j' : '0', 'K' : '-', 'k' : '_', 'L' : '+', 'l' : '=',
        'M' : '<', 'm' : ',', 'N' : '>', 'n' : '.', 'O' : '?', 'o' : '/', 'P' : ':', 'p' : ';',
        'Q' : '{', 'q' : '}', 'R' : '[', 'r' : ']', 'S' : '~', 's' : '`', 'T' : 'Á', 't' : 'á',
        'U' : '§', 'u' : 'ß', 'V' : 'Ú', 'v' : 'ú', 'W' : 'Ä', 'w' : 'ä', 'X' : 'Ö', 'x' : 'ö',
        'Y' : 'Ø', 'y' : 'ø', 'Z' : 'Ñ', 'z' : 'ñ'}
    
    try:
        encoded = open('encoded.txt', 'r')
    except Exception as err:
        print(err)
        
    for line in encoded:
        line = line.rstrip('\n')
        for letter in line:
            if letter != ' ':
                line = line.replace(letter, list(code.keys())[list(code.values()).index(letter)])
        print(line)

#------------------------------------------------------------------------------------------------#