# arrays vs hash map (dictionary)

#arrays
stock_prices = []
with open ("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])

# using a list is not effieicnt. If the file is huge and you are looking for something in the end
# then the complexity of the program is big (order of n)

# same thing can be done using a hash map
stock_prices = {} #replacing list with a dictionary
with open ("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

# stock_prices[March 9] will give output 302.0
# this uses complexity of order 1

# writing hash function
def get_hash():
    h = 0
    for char in key:
        h += ord(char) # ord = gives reminder
    return (h % 100)
