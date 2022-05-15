# calculate sum of 2 individual lists
from audioop import add


tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

# the noob way
tom_total = 0
for i in tom_exp_list:
    tom_total += i
print(tom_total)

joe_total = 0
for i in joe_exp_list:
    joe_total += i
print(joe_total)

# being a pro = using functions
def calculate_total(exp): # this is the function arguement
    # this is a documentation string to explain the function
    '''
    this function takes 1 arguement which is a list and calculates the sum
    of all the elements in the list
    '''
    total = 0
    for i in exp:
        total+= i
    return total # this is called the function return value

tom_total = calculate_total(tom_exp_list)
print("Tom's total is:", tom_total)

joe_total = calculate_total(joe_exp_list)
print("Joe's total is:", joe_total)

print("///////////////////////////////////////////////////////////")

total = 0  # global variable
def sum(a,b): # if you want default b=5, put it here like sum(a,b=5). If you don't pass the arguement, it will take 5. 
    # But if you will pass the arguement, it will take that
    total = a+b # total = local variable
    print("total inside the function:", total)
    return total

n = sum(5,6) # you can also put sum(b=7,a=6) if you want to give your own values defying the order in the function
print("Total:", n)
print("Total outside the function:", total)

print("/////////////////////////////////////////////////")


