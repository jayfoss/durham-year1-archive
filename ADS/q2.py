"""
Fastest test times for this implementation:
E216B PC running Linux - q3test(): 9s; count_ephemeral(1, 10000000, 4): 25s
Mira - q3test(): 13s; count_ephemeral(1, 10000000, 4): 29s
"""
def count_ephemeral(n1, n2, k):
    count = 0
    #Sequence cache
    seqCache = {}
    #Exponent cache
    expCache = {}
    for i in range(n1, n2):
        #Current sequence
        seq = []
        val = i
        """
        Micro-optimisation
        Only evaluate appending to sequence once
        """
        seqAppend = seq.append
        while val != 1 and not val in seq:
            """
            Check the sequence cache so we don't keep regenerating
            sequences
            """
            if val in seqCache:
                #Get the last element of the cached list which will have first value val
                last = seqCache[val][len(seqCache[val]) - 1]
                #If the last element was 1, we found an ephemeral from cache
                if last == 1:
                    count += 1
                    break
                else:
                    #If not, append the cached list to the end of the array and set val for continued run
                    seq += seqCache[val]
                    val = last
            else:
                seqAppend(val)
                temp = 0
                rem = val
                """
                Micro-optimisation. Marginally faster than casting to string,
                then list, then iterating over list and recasting to int
                """
                while rem > 0:
                    num = rem % 10
                    """
                    Check the exponent cache so we don't keep recalculating
                    """
                    if not num in expCache:
                        #Exponentiate the number
                        expCache[num] = num ** k
                    #Add the now, or previously, populate cache value to temp
                    temp += expCache[num]
                    #Perform integer division to actually get the remainder
                    rem = rem // 10
                #Set val for next run
                val = temp
        #If we ended on a 1, append the 1 to the sequence for use in cache by later iterations
        if val == 1:
            seqAppend(val)
            #Since a 1 is at the end, we found an ephemeral
            count += 1
        #Cache the current sequence
        seqCache[seq[0]] = seq
    return count
