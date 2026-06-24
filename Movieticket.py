age = int(input("Enter your age: "))
student = input("Are you a student? (Y/N): ")
 
if age < 13:
    price = 8
elif age >= 65:
    price = 10
else:
    price = 12
 
if student == "Y":
    price = price - 2
 
print("Ticket price: $", price)

#code update check