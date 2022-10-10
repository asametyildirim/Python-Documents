file1 = open('demo1.csv', 'r')
Lines = file1.readlines()

count = 0
degisken = []
for line in Lines:
    split1 = line.split(",")
    if count >0:

        #print(float(split1[3]))
        if float(split1[3]) >= 20.0 and float(split1[3]) <30.0:
            split1[3] = "a"
        elif float(split1[3]) >= 30.0 and float(split1[3]) <40.0:
            split1[3] = "b"
        elif float(split1[3]) >= 40.0 and float(split1[3]) < 50.0:
            split1[3] = "c"
        elif float(split1[3]) >= 50.0 and float(split1[3]) < 60.0:
            split1[3] = "d"
        elif float(split1[3]) >= 60.0 and float(split1[3]) < 70.0:
            split1[3] = "e"
        elif float(split1[3]) >= 70.0 and float(split1[3]) < 80.0:
            split1[3] = "f"
        elif float(split1[3]) >= 80.0 and float(split1[3]) < 90.0:
            split1[3] = "g"
        elif float(split1[3]) >= 90.0 and float(split1[3]) < 100.0:
            split1[3] = "h"
        elif float(split1[3]) >= 100.0 and float(split1[3]) < 110.0:
            split1[3] = "i"
        elif float(split1[3]) >= 110.0 and float(split1[3]) < 120.0:
            split1[3] = "j"
        elif float(split1[3]) >= 120.0 and float(split1[3]) < 130.0:
            split1[3] = "k"
        elif float(split1[3]) >= 130.0 and float(split1[3]) < 140.0:
            split1[3] = "l"


    degisken = split1[0] +","+ split1[1]+","+ split1[2]+","+ split1[3]+","+ split1[4]+","+ split1[5]+","+ split1[6]+","+ split1[7]
    with open('demo1.csv', 'a') as the_file:
        the_file.write(degisken)
        print(degisken)

    count += 1




"""
20-30 =a
30=-40 =b
40=-50 =c
50=-60 =d
60=-70 =e
70=-80 =f
80=-90 =g
90=-100 =h
100=-110=i
110=-120 =j
120=-130=k
130=-140=l
"""