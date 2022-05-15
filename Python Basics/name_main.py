def calculate_area(base, height):
    print("__name__: ", __name__)
    return 1/2*(base*height)

if __name__ == "__main__": # this thing is used as the entry point to any python program
    # just like C++/Java programs' entry point is main() program
    print("I am in name_main.py")
    a = calculate_area(10,20)
    print("area: ", a)
# __name__ is a pre-defined variable whose value is __main__ by default
'''
When is __name__ not __main__?
    When you are calling a function from another file
    then __name__ will be the file in which the function is being called into
'''
