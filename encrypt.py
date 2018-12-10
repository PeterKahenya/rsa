import random
import time
import math
from math import gcd

p=0
q=0
n=0
e=0
def isPrime(Number):
    return 2 in [Number,2**Number%Number]

def get_plain():
    file=open("plaintext.txt","r")
    original=file.read()
    file.close()
    plain_t=[ord(x) for x in original]
    return plain_t

def get_private(e,phiN,n):
    for x in range(1,phiN*phiN):
        if (e*x)%phiN==1:
            return x

def generate_keys():
    random.seed(time.time())
    primes = [i for i in range(1,100) if isPrime(i)]
    p=random.choice(primes)
    q=random.choice(primes)
    n=p*q
    phiN=(p-1)*(q-1)
    e = random.randrange(1, phiN)
    g = gcd(e, phiN)
    while g != 1:
        e = random.randrange(1, phiN)
        g = gcd(e, phiN)
    d=get_private(e,phiN,n)
    #print(" p="+str(p)+" q="+str(q)+" n="+str(n)+" phiN="+str(phiN)+" e="+str(e)+" d="+str(d))
    send_keys(e,n,d)
    return e,n,d

def encrypt():
    e,n,p=generate_keys()
    plain_t=get_plain()
    cipher_t=[]
    for p in plain_t:
        c=(p**e)%n
        cipher_t.append(c)
    cipher=''.join([chr(i) for i in cipher_t])
    send_cipher(cipher)
    print("encryption "+'\033[92m'+ " DONE \u2713"+ '\033[0m')

def send_cipher(cipher_t):
    file=open("ciphertext.txt","w")
    file.write(cipher_t)
    file.close()

def send_keys(e,n,p):
    f=open("public_keys.txt","w")
    keys=str(e)+","+str(n)
    f.write(keys)
    f.close()

    f=open("private_key.txt","w")
    keys=str(p)
    f.write(keys)
    f.close()

encrypt()
