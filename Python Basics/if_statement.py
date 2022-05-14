# even or off number
num = input("Enter a number:") # this is a string
num = int(num) # this converts the string to a number

if num%2==0:
    print("even")
else:
    print("odd")

print("/////////////////////////////////////////////////")

# is the dish name in the cuisine?
indian = ["samosa", "daal", "naan"]
chinese = ["egg roll", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input("enter a dish name")

if dish in indian:
    print("Indian")

elif dish in chinese:
    print("chinese")

elif dish in italian:
    print("italian")
else:
    print("not in store")

