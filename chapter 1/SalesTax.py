
# Prompt the user for the putchase ammount

purchaseAmout = eval(input("Enter the purchase amount: "))

tax = purchaseAmout * 0.06

print("Sales tax is", int(tax*100)/100.0) 