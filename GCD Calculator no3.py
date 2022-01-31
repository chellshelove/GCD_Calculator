# method to compute gcd ( Euclidean algo )

def computeGCD(x, y):
    while(y):
        x, y = y, x % y
    return x

a = 7289
b = 8029

# prints 12
print ("The gcd of a and b is : ",end="")
print (computeGCD(7289,8029))