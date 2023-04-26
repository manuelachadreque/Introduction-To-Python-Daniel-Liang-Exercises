#Prompt user for input

# get seconds
seconds = eval(input("enter an integer for secons: "))


#compute minutes
minutes =seconds//60

#compute remaining seconds

remainingSeconds = seconds % 60

print(seconds, "seconds are equivalent to ", minutes," and ", remainingSeconds, "seconds")