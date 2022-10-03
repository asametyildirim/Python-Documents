# I need a function of find prime number
def findPrimeNumber(Numbers):
    # Firstly divided number to 2
    primeNumber = True
    if Numbers == 1:
        primeNumber = False
        return primeNumber
    for i in range(2,Numbers):
        if Numbers % i == 0:
            primeNumber = False
            return primeNumber
    return primeNumber

def findLargestPrimeFactor2(Numbers):
    temporaryVariable = Numbers
    myArrays = []
    for i in range(2,Numbers):
        if temporaryVariable % i == 0:
            #myArrays.append(i)
            print(i)
            temporaryVariable = temporaryVariable /i
    #return myArrays



def findLargestPrimeFactor(Numbers):
    myPrimeNumberList = []
    for i in range(2,Numbers):
        if findPrimeNumber(i):
           myPrimeNumberList.append(i)
           print(i)
    #return myPrimeNumberList



sayi = 13195
sayi2 = 600851475143
findLargestPrimeFactor2(sayi2)
#print(findLargestPrimeFactor(sayi))

