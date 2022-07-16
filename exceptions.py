"""
try:
     number = int(input('Enter a number: '))
     number = number +2
     print(f'Result= {number}')
except:
     print("Error Occurred")


try:
     s1 = int(input("First Number: "))
     s2 = int(input("Second Number: "))

     result = s1/s2
     print("Result: ",result)

except ValueError:
     print("Please enter a numeric character.")
except ZeroDivisionError: #Error catching by error type
     print("You cannot divide a number by zero")
except:
     print("An error occurred")


try:
     print("Samet"+2)
except Exception as e: #printing the type of error to the screen
     print("Error occurred: ",e)


try:
     s1 = int(input("Enter a value: "))
except:
     print("There was an error")
finally:
     print("This part worked")
"""