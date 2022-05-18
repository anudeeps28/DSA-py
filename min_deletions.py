'''
We need to find the minimum number of times a string reduces to another string where there are all unique characters.
'''

def getMinDeletions(s): # "abadbsdaas" taken as input 

    # if there are no recurring string items, return 0
    if len(s) == len(set(s)):
        return 0

    # however, if there are recurring items, then:

    # declaring unique_char variable as a set
    unique_char = set()
    del_count = 0 # putting del_count to 0 at the start
 
    # iterating through each item in s string "abadbsdaas"
    for char in s:
        # checking for condition if a particular item is already in empty set unique_char
        if char in unique_char: 
            # if it is, then del_count increases by 1
            del_count += 1

        # this is so because there cannot be recurring items in a set

        # adding that item in unique)char
        unique_char.add(char)

        '''
        and because unique_char is a set, all items in it will be unique. If you add repeated items in it,
        it won't give any error, but will also not add in the set unique_char

        this is how we keep count of del_count (which is what we want)
        ''' 
    
    return del_count


if __name__ == "__main__":
    print(getMinDeletions("abadbsdaas"))
    
