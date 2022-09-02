def loop1(): #This is an example of a while loop
    #loop 1 accepts no arguments
    #it loops through 10 times calculating a running
    #total and outputs the total as it processes
    
    LOOP_END = 11
    counter = 1
    total = 0
    
    #start the loop
    while counter < LOOP_END:
        #as long as counter < 10 these will execute
        print("This loop has run", counter, "times.")
        total += counter
        
        #output a message with the running total
        print("The total of number 1 - 10 for this iteration is:", total)
        
        #increment the accumulator
        counter += 1
        
        #the loop statements are over, so it will return to the while statement
        #to test the condition again

def loop2(): #for loop example
    #loopo 2 accepts no arguments
    #it calculates a running total of numbers 1-10
    #and outputs the total
    
    LOOP_BEGIN= 1
    LOOP_END = 10
    total = 0
    
    for num in range(LOOP_BEGIN, LOOP_END + 1): #for loop to iterate from 1 - 10
        #as long as values remain between 1 (loop_begin) - 10(loop_end), iterate
        
        total += num #keep a running total of all values from 1 - 10
        
        print("The loop has iterated", num, "times.")
        print("The total for this iteration of all numbers 1-10 is:",  total)
