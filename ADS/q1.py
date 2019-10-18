def hash_quadratic(l):
    #Create a new list filled with - to represent blanks
    table = ['-']*19
    #Iterate through the provided list
    for i in range(0, len(l)):
        #Determine the position the key should go to (if there is space) in hash table
        pos = ((6 * l[i] + 3) % 19)
        finished = False
        step = 0
        """
        While a finished condition hasn't been reached, try placing the element
        at the next available location, increasing quadratically.
        """
        while not finished:
            newPos = ((pos + step ** 2) % 19)
            #If the new found position is available, use it and finish.
            if(table[newPos] == '-'):
                table[newPos] = l[i]
                finished = True
            #If we've gone through the whole hash table and there is no space, exit
            elif(step >= 19):
                finished = True
            #Increase the step so next quadratic number is tried on next run (if it occurs)
            step += 1
    return table

def hash_double(l):
    #Create a new list filled with - to represent blanks
    table = ['-']*19
    #Iterate through the provided list
    for i in range(0, len(l)):
        #Generate hash value using first hash function
        h1 = ((6 * l[i] + 3) % 19)
        #If there is space at that loc, place the key
        if(table[h1] == '-'):
            table[h1] = l[i]
        else:
            #If there is no space, generate the secondary function
            h2 = 11 - (l[i] % 11)
            finished = False
            step = 1
            #Try place at next available location, using secondary hash function and a step.
            while not finished:
                pos = (h1 + step * h2) % 19
                if(table[pos] == '-'):
                    table[pos] = l[i]
                    finished = True
                #If all positions have been tried, give up
                elif(step >= 19):
                    finished = True
                step += 1
    return table
