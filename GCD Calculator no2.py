def computeGCD(x, y):
  
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
              
    return gcd
  
a = 1274
b = 10505
  
# prints 12
print ("The gcd of a and b is : ",end="")
print (computeGCD(1274,10505))