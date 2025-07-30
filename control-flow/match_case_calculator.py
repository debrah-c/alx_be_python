num1 = float(input("Enter the first number:") )
num2 = float(input("Enter the second number:") )
operation = input("Choose the operation (+, -, *,/):")

match operation:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        if num2 == 0:
          print ("Cannot divide by 0")
        print(f"{num1 / num2} = {num1 / num2}")
    case _:
        print("Invalid operation")
    

        
        

