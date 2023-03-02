# Question: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
#basic function
expenses = [2200, 2350, 2600, 2130, 2190]
print (expenses)
#answer 1
extra_in_feb = expenses[1] - expenses[0]
print (extra_in_feb)
#answer 2
expense_in_first_quarter = expenses[0] + expenses[1] + expenses[2]
print (expense_in_first_quarter)
#answer 3
for i in range(len(expenses)):
    if expenses[i] == 2000:
        print ("You spent 2000 in this month")

    else:
        print("You did not spend 2000 in this month")
#answer 4
expenses.append(1980)
print (expenses)
#answer 5
expenses[3] = expenses [3] + 200
print(expenses)

#question 2
heros=['spider man','thor','hulk','iron man','captain america']
#answer 1
print(len(heros))
#answer 2
heros.append('black panther')
print (heros)
#answer 3
heros.remove('black panther')
heros.insert(3, 'black panther')
print (heros)
#answer 4
heros[1] = 'doctor strange'
print (heros)
#answer 5
print (sorted(heros))
print (dir(heros))

heros[1:3] = ['doctor strange']
print (heros)
heros.sort()
print(heros)

#question 3
arr = []
a = input ("Enter the maximum number")
for i in range(1,a,2):
    arr.append(i)

print (arr)

#this is goning to be fun!
