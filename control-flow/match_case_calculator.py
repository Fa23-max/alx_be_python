num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operator = input("Choose the operation (+, -, *, /):")
result = 0 
match operator:
    case "+" :
      result= num1 + num2 
    case "*" :
      result=num1 * num2
    case "-" :
      result =num1 - num2
    case "/" :
      if num1 == 0 or num2 == 0 :
        print("Cannot divide by zero")
      else :
        result = num1 / num2
    case _ : 
        print("cannot do operation")
        
print(f"The result is {result}.")        
      
