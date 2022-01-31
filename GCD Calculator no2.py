# method to compute gcd ( Euclidean algo )

def computeGCD(x, y):
    while(y):
        x, y = y, x % y
    return x

a = 1274
b = 10505

# prints 12
print ("The gcd of a and b is : ",end="")
print (computeGCD(1274,10505))