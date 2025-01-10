def perform_operation(num1, num2, operation):
    match operation:
      case "add" :
        result= num1 + num2 
      case "multiply" :
        result=num1 * num2
      case "subtract" :
        result =num1 - num2
      case "divide" :
        if num1 == 0 or num2 == 0 :
          result = "Cannot divide by zero"
        else :
          result = num1 / num2
      case _ : 
          result = "cannot do operation"
    return result

_all_ = perform_operation