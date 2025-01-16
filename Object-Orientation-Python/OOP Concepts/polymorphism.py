'''

    len() treating objects as per its class

'''

from telnetlib import BM


students = ['Anudeep', 'Shankshinee', 'Kaustubh']
uni = 'Purdue University'

# calculating count
print(len(students))
print(len(uni))

############################################################################################################

'''
    polymorphism in class methods
'''

class Ferrari:
    def fuel_type(self):
        print("petrol")

    def max_speed(self):
        print("max speed is 350")

class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

ferrari = Ferrari()
bmw = BMW()

# iterate objects of same type
for car in (ferrari,bmw):
    # calling methods without checking the class of the object
    car.fuel_type()
    car.max_speed()

############################################################################################################

# polymorphism is usually used with inheritence
