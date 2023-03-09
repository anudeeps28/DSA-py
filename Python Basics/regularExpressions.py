import re

names = ['Finn Blade', 
         'Gier Andres', 
         'HappyCodingRobot', 
         'Ron Cromberge', 
         'Sohil']


# find people with first and last names only
regex = '^\w+ \w+$'

for name in names:
    result = re.search(regex, name)
    if result:
        print(name)
        print("--------------")
        print(result) 