# classic example of for loop
exp = [2340, 2500, 2100, 3100, 2980]

# using noob way
'''because this will not work when we have thousand list items'''
# total = exp[0]  + exp[1] + exp[2] + exp[3] + exp[4]

total = 0
for item in exp:
    total += item
print(total)

print("///////////////////////////////////////////////////////////")

# print numbers 1-10 using range()
for i in range(1,11): # range(start,end+1); range (0,end+1) = range(end+1)
     print(i)
     print(i*i)

print("///////////////////////////////////////////////////////////")

# print the monthly expense along with the month number
exp_2 = [2340, 2500, 2100, 3100, 2980]
total_2 = 0

for i in range(len(exp_2)):
    print("Month:", i+1, "Expense:", exp_2[i])
    total_2 += exp_2[i]
print(total_2)

print("///////////////////////////////////////////////////////////")

# search the lost car key and stop when found searching
key_location = "chair"
locations = ["garage", "living room","chair", "closet"]

for i in locations:
    if i == key_location:
        print("key location found in", i)
        break # breaks out of for loop
    else:
        print("keys not found in", i)

# print the square of all numbers b/w 1-5 EXCEPT even numbers
for i in range(1,6):
    if i%2 == 0:
        continue # the code jumps into the next iterations (lines below this not executed)
    print(i*i)

print("///////////////////////////////////////////////////////////")

# while statement
i = 1
while i<=5:
    print(i)
    i += 1
    # if you do not increment this counter, it will be an infinite loop
    



