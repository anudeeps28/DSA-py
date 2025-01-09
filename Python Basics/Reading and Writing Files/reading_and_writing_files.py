# creating new file and writing content to it
from distutils.file_util import write_file


f = open("writing_file.txt", "w")  # open opens a new file for writing or reading; w = write
# the above line can be written as with open("writing_file.txt", "w") as f
# w = overwrite previous content
f.write("I love Python")
f.close() # closing file will shut down all the resources that OS is using

'''this is a good practice: when you open a file, you
should also close the file'''

# appending more to file
f = open("writing_file.txt", "a") # a = append  
f.write("\nI love C++")
f.close()

print("//////////////////////////////////////////////////////////")

# read file line by line
f = open("writing_file.txt") # f = fhandle = file handle (explained in UMich Course)
print(f.read())
f.close()

print("//////////////////////////////////////////////////////////")

# counting number of words in each line
f = open("writing_file.txt")
for line in f:
    words = line.split(" ") # split gives a list of words (a list of all items in the string) (words is an array)
    print(words)
    print(len(words))

print("//////////////////////////////////////////////////////////")

# writing the word count in a new file
f = open("writing_file.txt")
f_out = open("writing_files_word_count.txt", "w") # f_out = another file handle
for line in f:
    words = line.split(" ") # split gives a list of words (a list of all items in the string) (words is an array)
    f_out.write("wordcount:" + str(len(words))+line)   
    print(words)
    print(len(words))


# opening with 'with' if you don't want to open and close the file
with open("writing_file.txt", "r") as f:
    print(f.read())
print(f.closed) # shows if the file is close or not
# with statement automotically closes the file




