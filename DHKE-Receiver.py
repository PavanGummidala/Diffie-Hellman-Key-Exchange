#Diffie–Hellman Key Exchange Receiver

#First Alice and Bob agree on a Prime number: P, and a Base: G. These numbers are not secret, and can be known by Eve.P must be a prime number, and G is a Primitive root modulo.
P = 23 #PrimeNumber
G =5 #BaseNumber

#Receiver Secret Key
b=10

#Generate a key
y=(G**b)%P
print("Key which can be share to sender:",y)

#key which is shared by sender
x=8

#Generate a Final secret Key which will not be shared to anyone

K=(x**b)%P

print("Final secret key:",K)