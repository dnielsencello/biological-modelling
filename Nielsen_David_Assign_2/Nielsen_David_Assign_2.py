#Looping and Branching Homework

# Problem 1
def executeBranch(x,y,z):
    if y > z:
        z=z*3
        if z < x:
            x = x*3
        else:
            y = y/4
    else:
        y = y*2
        if y > x:
            x = x*4
        else:
            z = x/3
    
    return x, y, z


# Problem 2
def executeLoop(x):
    if type(x) == int and x > 0:
        while x < 236:
            x = x*4
        while x > 14:
            x = x/3
        return x
    else:
        return type(x)

# Problem 3       
# finds factorial of a number passed into it
'''
This uses a recursive method to find the factorial of the number  
'''


# Problem 4
# determines if a number is prime
'''
This function loops through every number and uses the mod function to determine
if it is a factor of the number, if there are no factors of the number other 
the number 1 or the number itself then it is a prime number. 
'''
def isPrime(num):
    if num > 1:
        for i in range(2,int(num)):
            if (num%i) == 0:
                return False
        return True

'''
To test functions written, please print the return values here

'''
if __name__ == "__main__":
    x = 3
    y = 4
    z = 5 
    
    print("With the inputs x=" + str(x) + ",y=" + str(y) + ",z=" + str(z) + ", the output of executeBranch is " + str(executeBranch(x, y, z)))
    
    x = 3
    
    print("With the input of x=" + str(x) + " the executeLoop output is " + str(executeLoop(x)))

    num = int(input("Problem 3: Input the number you wish to find the factorial for: "))
    print("The Facotorial of " + str(num) + " is " + str(findFactorial(num)))

    num = int(input("Problem 4: Input a number that is a prime number: "))
    if isPrime(num) == True:
        print("True, " + str(num) + " is a prime number")
    else:
        print("False, " + str(num) + " is not a prime number")

# Example 
#print('Problem 1',executeBranch(3,12,1))