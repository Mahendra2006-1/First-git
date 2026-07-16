def calculate(a,b):
    sum = a+b
    diff = a-b
    multiplication = a*b
    division = a/b

    return sum,diff,multiplication,division


result = calculate(10,5)
print("addition of two numbers is: ",result[0])
print("subtraction  of two numbers is: ",result[1])
print("Multiplication of two numbers is: ",result[2])
print("Division of two numbers is: ",result[3])
