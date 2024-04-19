from add import add
from sub import sub
from mul import mul
from div import div

print("Welcome to Calculator")
a=int(input("Enter first number\n"))
b=int(input("Enter second number\n"))
c=input("Enter operation\n")
if c=="+":
    print(add(a,b))
elif c=="-":
    print(sub(a,b))
elif c=="*":
    print(mul(a,b))
elif c=="/":
    print(div(a,b))
else:
    print("Wrong Choice")
