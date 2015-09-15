# Dan Nguyen HW 2: RSA Cryptography

import sys
from random import randint
import time
from fractions import gcd


def main(argv):
    global totientN
    global nprimes
    global primes
    n = input('Enter how many digits would you like prime numbers p and q to be: ')
    
    primeTime = time.time()
    nprimes = []
    primes = [] #Create an array of prime numbers
    
    for num in range(1,10**n): #Digit span. 10^3 --> 3 digit long prime numbers.
        prime = True
        for i in range(2,num):
            if (num%i==0):     # modulus of 0 implies not prime
                prime = False
        if prime:
           primes.append(num)  # Add prime numbers to the prime array
           
    for i in range(0, len(primes)-1): # remove the primes that are shorter than then desired bit length
        if (numLen(primes[i]) == n):  # If n = 2, remove all single digit primes
            nprimes.append(primes[i])
            i+= 1   
    p = nprimes[randint(0, len(nprimes)-1)]
    q = nprimes[randint(0, len(nprimes)-1)]
    

    
    # print primes  # Print the prime array
    # print nprimes # Print the array without the unwanted digit primes
    print "p:          ",p
    print "q:          ",q
    N = p*q
    print "N:          ", N

    totientN = (p-1)*(q-1)
    print "Totient(N): ", totientN
    
    e = public_key(n, nprimes, totientN)  
    print "e:          ", e
    
    privateKey = modularInverse(e, totientN)
    
    primeTimeEnd = time.time
    primeGenerationTime = primeTimeEnd() - primeTime
    
    encode = input('Enter a number to be encoded: ')
    
    encodeTime = time.time()
    c = encode ** e % N
    encodeTimeEnd = time.time
    encodingTime = encodeTimeEnd() - encodeTime
    
    print "c:          ", c     
    
    
    decryptTime = time.time()
    decrypt = c ** privateKey % N
    decryptTimeEnd = time.time
    decryptingTime = decryptTimeEnd() - decryptTime
    
    print "decrypting------------------>",decrypt
    print("Generating prime numbers took --- %s seconds ---" % (primeGenerationTime)) 
    print("Encoding x = 2015 to y took   --- %s seconds ---" % (encodingTime)) 
    print("Decrypting y --> message took --- %s seconds ---" % (decryptingTime)) 

    
def public_key(n, nprimes, totientN): # Generate e
    key = nprimes[randint(0, len(nprimes)-1)]
    if (key > totientN or gcd(key, totientN) != 1):
        public_key(n, nprimes, totientN)
    else:
        return key

def modularInverse(e, totientN):
    t = 0
    newt = 1    
    r = totientN
    newr = e
    while (newr != 0):
        quotient = r / newr
        (t, newt) = (newt, t - quotient * newt) 
        (r, newr) = (newr, r - quotient * newr)
    if (r > 1):
        return "e is not invertible"
    if (t < 0):
        t = t + totientN
    return t
    
    
    
    
    
    
    
def numLen(number):
    return len(str(number))

if __name__ == "__main__":
    main(sys.argv)
    # args = sys.arv[1]
    # args = int(args)
    # main(args)