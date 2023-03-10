import csv

# we could do strings split method on each line, but this csv module makes it really easy to parse these files!

# # reading file
# with open('names.csv', 'r') as f:
#     csvReader = csv.reader(f) #csvReader is just an object in the memory

#     for line in csvReader:
#         print(line)
#         print("Email: ", line[2])
#         print("####")

# writing a new CSV file
# with open('names.csv', 'r') as f:
#     csvReader = csv.reader(f) 

#     with open('newNames.csv', 'w') as newFile:
#         csvWriter = csv.writer(newFile, delimiter='\t') # we want to store the enteries into the new file seperated by '-'

#         for line in csvReader:
#             csvWriter.writerow(line)

# if we don't specify the delimiter while reading, it will give just 1 whole chunk
# with open('newNames.csv', 'r') as f:
#     csvReader = csv.reader(f) # give delimiter as csvReader = csv.reader(f, delimiter = '\t')

#     for line in csvReader:
#         print(line)

# reading using dictionary reader and writer
# with open('names.csv', 'r') as f:
#     csvReader = csv.DictReader(f) 

#     for line in csvReader:
#         print(line)
#         print(line['email'])
#         print("###")

# writing using dictionary reader and writer
with open('names.csv', 'r') as f:
    csvReader = csv.DictReader(f) 

    with open('newNames.csv', 'w') as newFile:
        fieldNames = ['first_name', 'last_name', 'email'] # remove 'email' also if you want that also

        csvWriter = csv.DictWriter(newFile, fieldnames=fieldNames, delimiter= '\t')
        csvWriter.writeheader()

        for line in csvReader:
            # del line['email']
            csvWriter.writerow(line)
