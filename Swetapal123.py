# OPERATOR
a = float(input("Enter First No. "))
b = float(input("Enter second No. "))
op = input("Enter the operator(+,-,*,/):")
if op == "+":
    print("result:",a+b)
elif op == "-":
    print("result:",a-b)
elif op == "*":
    print("result:",a*b)
elif op == "/":
    if b!= 0:
        print("result:",a/b)
    else:print("cannot divide by zero: ")
else:print("invalid operator")

# PERSON DETAILS
emailid = input("enter your id: ")
name = input("enter your name: ")
age = input("enter your age: ")
ocupation = input("enter your ocupation: ")
city = input("enter your city: ")
print("Hello," , id)
print("name:" , name)
print("age:" ,age)
print("ocupation:", ocupation)
print("city:" ,city)

# FOR EXIT
while True:
    user_input = input("enter a command ('exit'): ").lower()
    if user_input == 'exit':
        print("exiting the program. ")
        break
    
