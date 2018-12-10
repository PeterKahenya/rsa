
e=0
n=0
d=0
def get_keys():
    f=open("private_key.txt","r")
    d=int(f.read())
    f.close()
    f=open("public_keys.txt","r")
    keys=f.read().split(",")
    f.close()
    e=int(keys[0])
    n=int(keys[1])
    return e,n,d

def get_cipher_text():
    file=open("ciphertext.txt","r")
    original=file.read()
    cipher_t=[ord(x) for x in original]
    return cipher_t

def decrypt():
    e,n,d=get_keys()
    ciphertext=get_cipher_text()
    plain = [chr((char ** d) % n) for char in ciphertext]
    plain = ''.join(plain)
    print("The message is :"+'\033[92m'+plain+'\033[0m')


decrypt()
