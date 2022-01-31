def computeGCD(x, y):
  
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
              
    return gcd
  
a = 7289
b = 8029
  
# prints 12
print ("The gcd of a and b is : ",end="")
print (computeGCD(7289,8029))