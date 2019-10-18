#function HammingG
#input: a number r
#output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code
def hammingGeneratorMatrix(r):
    n = 2**r-1
    
    #construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2**(r-i-1))
    for j in range(1,r):
        for k in range(2**j+1,2**(j+1)):
            pi.append(k)

    #construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i+1))

    #construct H'
    H = []
    for i in range(r,n):
        H.append(decimalToVector(pi[i],r))

    #construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n-r):
        GG.append(decimalToVector(2**(n-r-i-1),n-r))

    #apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    #transpose    
    G = [list(i) for i in zip(*G)]

    return G


#function decimalToVector
#input: numbers n and r (0 <= n<2**r)
#output: a string v of r bits representing n
def decimalToVector(n,r): 
    v = []
    for s in range(r):
        v.insert(0,n%2)
        n //= 2
    return v

def message(a):
    l = len(a)
    #If the input is invalid, discard. No message can be calculated
    if not type(a) == list or l < 1:
        return []
    m = []
    #Determine the r value based on message length
    r = 2
    while(2**r - 2 * r - 1 < l):
        r += 1
    k = 2 ** r - r - 1
    #Convert the input length to a binary list of length r
    m += decimalToVector(l, r)
    #Append the input to the message
    m += a
    #Add the required 0 padding to make a valid message
    m += [0]*(k - len(m))
    return m

def hammingEncoder(m):
    #Calculate r value for the message
    r = 2
    while(2**r - r - 1 < len(m)):
        r += 1
    #Get the generator matrix
    g = hammingGeneratorMatrix(r)
    #If the length of the message does not match length of generator matrix,
    #for the calculated r value, it is invalid.
    if len(g) != len(m):
        return []
    c = []
    #Encode the message using multiplication mod 2
    #Need to iterate for as many times as there are rows in gen matrix
    for i in range(len(g[0])):
        total = 0
        for j in range(len(g)):
            total += (g[j][i] * m[j]) % 2
        c.append(total % 2)
    return c

def hammingDecoder(v):
    r = 2
    while(2 ** r - 1 < len(v)):
        r += 1
    H = []
    #Determine the parity check matrix
    for i in range(1, 2 ** r):
        H += [decimalToVector(i, r)]
    #If the length of encoded message does not match parity check mat length, invalid
    if len(v) != len(H):
        return []
    vHT = [0]*len(H[0])
    #Determine v * H transpose using mod 2 multiplication and addition
    for i in range(len(H[0])):
        for j in range(len(v)):
            vHT[i] = (vHT[i] + ((v[j] * H[j][i]) % 2)) % 2
    #If the v multiplied by H transpose is 0 vector, v is a codeword so return it
    isZero = True
    for i in range(len(vHT)):
        if vHT[i] != 0:
            isZero = False
    if isZero:
        return v
    #Determine offset number
    i = 0
    for j in range(len(vHT)):
        i += (2 ** j * vHT[len(vHT) - j - 1])
    c = v
    #Flip the offset bit (could also do this with mod 2 addition)
    if c[i - 1] == 1:
        c[i - 1] = 0
    else:
        c[i - 1] = 1
    return c

def messageFromCodeword(c):
    r = 2
    while(2 ** r - 1 < len(c)):
        r += 1
    #Get the generator matrix to perform an easy validity check
    g = hammingGeneratorMatrix(r)
    m = []
    if len(c) != len(g[0]):
        return []
    #Get the bits from every 2^n element. Use bitwise AND to do this
    for i in range(len(c)):
        pos = i + 1
        if (pos & (pos - 1)) != 0:
            m.append(c[i])
    return m

def dataFromMessage(m):
    r = 2
    while(2 ** r - r - 1 < len(m)):
        r += 1
    l = []
    #Get the list part that represents data length
    l += m[0:r]
    l.reverse()
    n = 0
    #Determine data length
    for i in range(len(l)):
        n += (2 ** i) * l[i]
    #If there is less array left than message length, invalid
    if len(m[r:]) < n:
        return []
    #Check that end of message is only padded with zeros
    if m[r + n:].count(0) != len(m[r + n:]):
        return []
    #Strip off trailing 0s after data
    return m[r:r + n]

def repetitionEncoder(m, n):
    if len(m) != 1:
        return []
    return [m[0]] * n

def repetitionDecoder(v):
    #Count 0s and 1s. Return larger count. If equal, invalid
    c0 = v.count(0)
    c1 = v.count(1)
    if c1 > c0:
        return [1]
    elif c0 > c1:
        return [0]
    return []
