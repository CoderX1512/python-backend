# math_operations.py
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error:Division by zero"
    return a/b

if __name__ == "__main__":
    #This code will run when math_operations.py is the main program
    print('This script is the main program')