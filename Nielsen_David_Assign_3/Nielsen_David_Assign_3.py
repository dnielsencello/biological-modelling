import numpy as np

def primeListGen():
    pList = [x for x in range(2, 10000) if all(x % y != 0 for y in range(2, x))]
    return(pList)  

def findFactorial(num):
    if type(num) == int and num > 0:
        if num == 1:
            return num
        else:
            return num*findFactorial(num-1)
    else:
        return("not an integer")
    
def createMatrix():
    listTwo = [[j+i for i in range(1,4)] for j in [0,3,6]]
    return listTwo

def createMatrix2():
    numpyArray = np.zeros([21,3],int)
    numpyArray[1:,0] = [i for i in range(1,21)]
    numpyArray[1:,1] = [numpyArray[i][0]*3 for i in range(1,21)]
    numpyArray[1:,2] = [2*numpyArray[i-1][1] for i in range(1,21)]
    return numpyArray
               
if __name__ == "__main__":
    primeList = primeListGen()
    print('Problem 1A. The length of the prime number list is: '+  str(len(primeList)) +'\n')
    print('Problem 1B. The last ten digits of the prime number list are: \n' + '\n'.join(str(i) for i in primeList[-10:]) +'\n')
    factorialList = [findFactorial(x) for x in range(1,100)]
    print('Problem 2A. The first ten integers in the factorial list are: \n' + '\n'.join(str(i) for i in factorialList[:10]) +'\n')
    print('Problem 2B. The last ten integers in the factorial list are: \n' + '\n'.join(str(i) for i in factorialList[-10:]) + '\n') 
    matrix2D = createMatrix()
    print('Problem 3. This is the 2D Matrix: \n' + '\n'.join(str(i).strip('[]') for i in matrix2D) +'\n')
    npList = createMatrix2()
    npList = npList.tolist()
    print('Problem 4. This is the numpy matrix: \n' + '\n'.join(str(i).strip('[]') for i in npList) + '\n')