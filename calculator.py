num1=float(input("Enter The Number One : "))
ope=input("Enter Operator : ")
num2=float(input("Enter The Second Number : "))

if ope=="+":
    print("Result : ",num1+num2)
elif ope=="-":
    print("Result : ",num1-num2)
elif ope=="*":
    print("Result : ",num1*num2)
elif ope=="/":
    if num2==0:
        print("Devision Error!")
    else:
        print("Result : ",num1/num2)
else:
    print("Invalid Operator!")