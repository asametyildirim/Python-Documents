import threading


def myFunction1(variable):
    variable= variable+1
    print(degisken)

def myFunction2(variable):
    variable = variable +2
    print(degisken)

if __name__ == "__main__":
   t1 = threading.Thread(target=myFunction1, args=(variable,))
   t2 = threading.Thread(target=myFunction2, args=(variable,))
   t2.start()
   t1.start()
   print("Done!")
