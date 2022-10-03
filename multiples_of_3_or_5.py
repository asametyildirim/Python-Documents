def Multiples(toNumber):
    total = 0

    for i in range(0,toNumber):
        if (i % 3 == 0) or (i % 5 == 0):
            #print(f"{i} Bölündü")
            total = total + i

    return total

print(Multiples(1000))





