def CreateFibo(toNumber):
    number1 = 1
    number2 = 2
    newNumber = 3

    total = 2
    for i in range(0, toNumber):

        newNumber = number1 + number2
        if newNumber > 4000000:
            return total
            print("yazma")
            Break
        print(newNumber)
        if newNumber % 2 == 0:
            total = total + newNumber

        number1 = number2
        number2 = newNumber

    return total


print(CreateFibo(1000))




