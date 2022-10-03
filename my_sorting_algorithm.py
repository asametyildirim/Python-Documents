def sortByArray(MyArray):

    for i in range(0,len(MyArray)):

        min_value = i

        for j in range(i+1,len(MyArray)):
            if MyArray[min_value] > MyArray[j]:
                min_value = j
        MyArray[min_value],  MyArray[i] = MyArray[i], MyArray[min_value]
    return MyArray


Array = [99,34,423,1,24,6,7,8743,23,42,42,565,46,34,423,46,345,423,423,63,787986,5,235,5635,36,]
print(sortByArray(Array))

