def func():
     print("My first function")
func()

def func(name):
     print("Hello "+name)
func("Samet")

def func(number1,number2):
     total =number1 +number2
     return total
incoming_result = func(3,4)
print(f"Result = {incoming_result}")