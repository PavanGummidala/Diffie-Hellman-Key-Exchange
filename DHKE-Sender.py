#Diffie–Hellman Key Exchange Sender

#First Alice and Bob agree on a Prime number: P, and a Base: G. These numbers are not secret, and can be known by Eve.P must be a prime number, and G is a Primitive root modulo.
P = 23 #PrimeNumber
G =5 #BaseNumber

#Sender Secret Key
a=6

#Generate a key
x=(G**a)%P
print("Key which can be share to Receiver:",x)

#key which is shared by Receiver
y=9

#Generate a Final secret Key which will not be shared to anyone

K=(y**a)%P

print("Final secret key:",K)