op = input("Enter an operator(+,-,*,/): ")
n1= int(input("Enter the first number: "))
n2= int(input("Enter the 2nd number: "))

if op == "+":
    result= n1+n2
    print(round(result,2))
elif op == "-":
    result= n1-n2
    print(round(result,2))
elif op == "*":
    result= n1*n2
    print(round(result,2))
elif op == "/":
    result= n1/n2
    print(round(result,2))
else :
    print(f"{op} is an invalid operator")
