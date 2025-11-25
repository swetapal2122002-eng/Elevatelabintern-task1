'''while True:
    user_input = input("Enter something (or type 'exit' to stop): ")

    if user_input.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break

    elif user_input.isdigit():
        print("You entered a number.")

    elif user_input.isalpha():
        print("You entered alphabets.")

    else:
        print("You entered a mix of characters.")'''

for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

units = int(input("Enter the units consumed:"))
bill = 0
if units <=  100:
    bill = units*5
elif units <= 200:
    bill = (100*5)+(units-100)*7
else:
    bill (100*5)+(100*7)+(units-200)*10
print("total bill:rs.",bill)

