op= input("Enter op(+,-,*,/):")
a=int(input("Enter a:"))
b=int(input("Enter b:"))

if op == "+":
    print(a+b)
if op == "-":
    print(a-b)
if op == "*":
    print(a*b)
if op == "/":
    if b == 0:
        print("error-0")
    else :
        print(a/b)


