"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] # create an emply sales people list
melons_sold = [] # create an empty list for melons sold

# open the file
f = open('sales-report.txt')
# iterating through each line in the file
for line in f:
    # remove all white spaces
    line = line.rstrip()
    # create a list of data
    entries = line.split('|')
    # get the name of the sales person 
    salesperson = entries[0]
    # get the number of melons that has been sold by the sales person
    melons = int(entries[2])
    # check if salesperson is in the salespeople list
    if salesperson in salespeople:
        # find the position of the salesperson in the list
        position = salespeople.index(salesperson)
        # use the position to index into melons
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# loop over salespeople and use it to index into salespeople and melons sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
