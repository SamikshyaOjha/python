#handling multiple error types
try:
    a=int(input("enter a number:"))
    b=int(input("enter a divison:"))
    result=a/b
    print(f"Result: { result}")
except ZeroDivionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter a valid number")
except Exception as e:
    print(f"Unexpected error:{e}")