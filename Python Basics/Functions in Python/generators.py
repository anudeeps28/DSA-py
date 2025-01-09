from re import A


def remote_control_next():
    yield "cnn" #yield is similar to return but it does not close all resources and does not clear the memory
    yield "espn"

itr = remote_control_next()
print(itr) 

print(next(itr))
print(next(itr))

# this is useful when you have a long list of values and you
# do not want to return them in one shot
# returning all = takes up a lot of memory 

# another way
for c in remote_control_next():
    print(c)

# creating fibonacci sequence using generators
def fib():
    a,b = 0,1
    while True: # infinite loop
        yield a
        a,b = b, a+b

for f in fib():
    if f > 50: # putting limits on the loop
        break
    print(f)

