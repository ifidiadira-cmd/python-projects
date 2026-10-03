num = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
operation = input("Pick a basic operation(multiply, add, subtract, divide): ")

valid_ops = ["multiply", "add", "subtract", "divide"]

while operation not in valid_ops:
    print("Invalid operation, pick another")
    operation = input("Pick a basic operation(multiply, add, subtract, divide): ")
    
answer = None

if operation == "add":
    answer = num + num2
    print(answer)
elif operation == "subtract":
    answer = num - num2
    print(answer)
elif operation == "multiply":
    answer = num*num2
    print(answer)
elif operation == "divide":
    if num2 == 0:
        print("Cannot divide by 0, pick another number")
    else:
        answer = num/num2
        print(answer)

