print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
option= int(input("Choose an operation: "))

if (option in [1,2,3,4]):
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))

    if (option==1):
        print("The result of the operation is: ",a+b)
    elif (option==2):
        print("The result of the operation is: ",a-b)
    elif (option==3):
        print("The result of the operation is: ",a*b)
    elif (option==4):
        print("The result of the operation is: ",a/b)
else:
    print("Invalid operation")