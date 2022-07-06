# Python3 implementation of the approach
import math


# Function that returns True if n
# is prime else returns False
def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False

    return True


# Function to return the smallest
# prime number greater than N
def nextPrime(N):
    # Base case
    if (N <= 1):
        return 2

    prime = N
    found = False

    # Loop continuously until isPrime returns
    # True for a number greater than n
    while (not found):
        prime = prime + 1

        if (isPrime(prime) == True):
            found = True

    return prime


# Both the persons will be agreed upon the
# public keys G and P
# A prime number P is taken
print("Enter a quite large prime number")
P = int(input())

print("Enter another quite large prime number")
G = int(input())


print('The Value of P is :%d' % (P))
print('The Value of G is :%d' % (G))

# Alice will choose the private key a
print("Hey!! Alice .. choose your private key")
a = int(input())
print('The Private Key a for Alice is :%d' % (a))

# gets the generated key
x = int(pow(G, a, P))

# Bob will choose the private key b
print("Hey!! Bob .. choose your private key")
b = int(input())
print('The Private Key b for Bob is :%d' % (b))

# gets the generated key
y = int(pow(G, b, P))

# Secret key for Alice
ka = int(pow(y, a, P))

# Secret key for Bob
kb = int(pow(x, b, P))

print('Secret key for the Alice is : %d' % (ka))
print('Secret Key for the Bob is : %d' % (kb))

key=ka

prime1=107
prime2=nextPrime(key)
if(prime2==prime1):
    prime2=nextPrime(prime1)

#MD5 implementation

def binaryToDecimal(n):
    num = n
    dec_value = 0

    # Initializing base
    # value to 1, i.e 2 ^ 0
    base1 = 1

    len1 = len(num)
    for i in range(len1 - 1, -1, -1):
        if (num[i] == '1'):
            dec_value += base1
        base1 = base1 * 2

    return dec_value


def leftrotate(x, c):
    return (x << c) or (x >> (32 - c))

def MD5Function(str):
    #: All variables are unsigned 32 bit and wrap modulo 2^32 when calculating
    #import math



    K = []
    msg = "chayan"
    msg = str
    res = ''.join(format(ord(i), '08b') for i in msg)

    # s specifies the per-round shift amounts
    # print(res)
    # print(len(res))
    s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22]

    for i in range(0, 4):
        s.append(5)
        s.append(9)
        s.append(14)
        s.append(20)
    for i in range(0, 4):
        s.append(4)
        s.append(11)
        s.append(16)
        s.append(23)
    for i in range(0, 4):
        s.append(6)
        s.append(10)
        s.append(15)
        s.append(21)

    # Use binary integer part of the sines of integers (Radians) as constants:
    for i in range(0, 64):
        K.append(((math.floor(232 * abs(math.sin(i + 1))))))
    # end for

    # Initialize variables:
    a0 = 0x67452301  # A
    b0 = 0xefcdab89  # B
    c0 = 0x98badcfe  # C
    d0 = 0x10325476  # D
    # print(type(a0))

    # Pre-processing: adding a single 1 bit
    # append "1" bit to message
    res += ('1')
    # Notice: the input bytes are considered as bits strings,
    #  where the first bit is the most significant bit of the byte.[51]

    # Pre-processing: padding with zeros
    # append "0" bit until message length in bits ≡ 448 (mod 512)
    # print(type(res))
    org_len = len(res)

    while (1):
        length = len(res)
        if (length % 512 == 448):
            break;

        res += ('0');

    # print(len(res))
    for i in range(63, -1, -1):
        k = org_len >> i
        if (k & 1):
            res += '1'
        else:
            res += '0'

    new_len = len(res)
    # print(len(res))
    # print(res)

    for chunk in range(0, new_len, 512):
        M = []

        for j in range(0, 512, 32):
            tmp = ""
            for it in range(0, 32):
                ind = chunk + j + it

                tmp += res[ind]

            M.append(tmp)

        A = a0
        B = b0
        C = c0
        D = d0
        # print(len(M))
        for i in range(0, 64):
            F = 0
            g = 0
            if (i >= 0) and (i <= 15):
                F = (B and C) or ((not B) and D)
                g = i
                # print("AA",end=" ")
                # print(g)

            elif (i >= 16) and (i <= 31):
                F = (D and B) or ((not D) and C)
                g = (5 * i + 1) % 16
                # print("BB", end=" ")
                # print(g)
            elif (i >= 32) and (i <= 47):
                F = B ^ C ^ D
                g = (3 * i + 5) % 16
                # print("CC", end=" ")
                # print(g)
            elif (i >= 48) and (i <= 63):
                F = C ^ (B or (not D))
                g = (7 * i) % 16
                # print("DD", end=" ")
                # print(g)

            # print(type(F))
            # print(type(A))
            # print(type(K))
            # print(type(M))
            # int_msg = ''.join(format(ord(i), '08b') for i in M[g])
            new_val = binaryToDecimal(M[g])
            # print(g)
            # print(M[g])
            F = F + A + K[i] + new_val
            # print(F)

            A = D
            D = C
            C = B
            B = B + leftrotate(F, s[i])
        a0 = a0 + A
        b0 = b0 + B
        c0 = c0 + C
        d0 = d0 + D

    #print("MD5 Hash is the following-")
    ans = []
    ans.append(a0)
    ans.append(b0)
    ans.append(c0)
    ans.append(d0)
    #print(ans)
    return ans


'''
WELCOME TO THE RSA ENCRYPTOR. THIS IS AN INTERACTIVE TOOL USED TO ENCRYPT OR DECRYPT A MESSAGE USING THE FAMOUS RSA ALGORITHM.

'''

#import math

print("RSA ENCRYPTOR/DECRYPTOR")
print("*******************")

# Input Prime Numbers
#print("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")
p = prime1
q = prime2
print("*******************")

# Check if Input's are Prime
'''THIS FUNCTION AND THE CODE IMMEDIATELY BELOW THE FUNCTION CHECKS WHETHER THE INPUTS ARE PRIME OR NOT.'''


def prime_check(a):
    if (a == 2):
        return True
    elif ((a < 2) or ((a % 2) == 0)):
        return False
    elif (a > 2):
        for i in range(2, a):
            if not (a % i):
                return false
    return True


check_p = prime_check(p)
check_q = prime_check(q)
while (((check_p == False) or (check_q == False))):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)

# RSA Modulus
'''CALCULATION OF RSA MODULUS 'n'.'''
n = p * q
#print("RSA Modulus(n) is:", n)

# Eulers Toitent
'''CALCULATION OF EULERS TOITENT 'r'.'''
r = (p - 1) * (q - 1)
#print("Eulers Toitent(r) is:", r)
#print("*******************")

# GCD
'''CALCULATION OF GCD FOR 'e' CALCULATION.'''


def egcd(e, r):
    while (r != 0):
        e, r = r, e % r
    return e


# Euclid's Algorithm
def eugcd(e, r):
    for i in range(1, r):
        while (e != 0):
            a, b = r // e, r % e
            #if (b != 0):
                #print("%d = %d*(%d) + %d" % (r, a, e, b))

            r = e
            e = b


# Extended Euclidean Algorithm
def eea(a, b):
    if (a % b == 0):
        return (b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s - ((a // b) * t)
        #print("%d = %d*(%d) + (%d)*(%d)" % (gcd, a, t, s, b))
        return (gcd, t, s)


# Multiplicative Inverse
def mult_inv(e, r):
    gcd, s, _ = eea(e, r)
    if (gcd != 1):
        return None
    else:
        #if (s < 0):
            #print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d." % (s, s, s % r))
        #elif (s > 0):
            #print("s=%d." % (s))
        return s % r


# e Value Calculation
'''FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME.'''
for i in range(1, 1000):
    if (egcd(i, r) == 1):
        e = i
#print("The value of e is:", e)
#print("*******************")

# d, Private and Public Keys
'''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''
#print("EUCLID'S ALGORITHM:")
eugcd(e, r)
#print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.")
#print("*******************")
#print("EUCLID'S EXTENDED ALGORITHM:")
d = mult_inv(e, r)
#print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
#print("The value of d is:", d)
#print("*******************")
public = (e, n)
private = (d, n)
#print("Private Key is:", private)
#print("Public Key is:", public)
#print("*******************")

# Encryption
'''ENCRYPTION ALGORITHM.'''


def encrypt(pub_key, n_text):
    e, n = pub_key
    x = []
    m = 0
    for i in n_text:
        m=ord(i)
        c = (m ** e) % n
        x.append(c)
    return x


# Decryption
'''DECRYPTION ALGORITHM'''


def decrypt(priv_key, c_text):
    d, n = priv_key
    txt = c_text.split(',')
    x = ''
    m = 0
    for i in txt:
        m = (int(i) ** d) % n
        x+=chr(m)
    return x





hash_value=MD5Function("LEETCODE")
while(True):
    # Choose Encrypt or Decrypt and Print
    choose = input("Type '1' for encryption and '2' for decrytion.")
    if (choose == '1'):
        # Message
        message = input("Enter the string")
        print("Your message is:", message)
        enc_msg = encrypt(public, message)
        print("Your encrypted message is:", enc_msg)
        print("Thank you for using the RSA Encryptor. Goodbye!")
        hash_value=MD5Function(message.upper())
    elif (choose == '2'):
        # Message
        message = input("Enter the numbers of the cipher text and separate them with comma(,)")
        print("Your message is:", message)
        print("Your decrypted message is:", decrypt(private, message))
        decrypted_text = decrypt(private, message)
        hash_value2 = MD5Function(decrypted_text)
        if (hash_value2 == hash_value):
            print("Authentication Successful")
        print("Thank you for using the RSA Encryptor. Goodbye!")
    else:
        print("You entered the wrong option.")
        print("Thank you for using the RSA Encryptor. Goodbye!")
        break







#print(cipher_text)