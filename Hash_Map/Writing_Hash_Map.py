# writing hash function

class HashTable: 
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)] # initializing array of 100 elements with each value None

    def get_hash(self,key):
        h = 0
        for char in key:
            h+= ord(char)
            return h % self.MAX

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

# __setitem__ and __getitem__ are standard python operators
# creating objects class HashTable

t=HashTable()
t['march 6'] = 130
t['march 17'] = 20

t.arr 
    #this will show that all the above got stored

t['march 17']
    # this will show 20

del t['march 6']
    # this will delete that item

# by writing this class, we implemented a dictionary


