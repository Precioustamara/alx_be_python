def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
          return 'it cannot divide by zero'
        else:
          return num1 / num2
    else:
       return 'invalid'
    
if __name__ == "__main__":
   perform_operation(5, 10, 'add')
        
