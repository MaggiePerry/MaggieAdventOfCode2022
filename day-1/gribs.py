# Function to add total sum of array values
def sum(foods) :
    total = 0

    for food in foods :
        total += int(food)
    return total

# Open inputs.txt
with open('day-1/input.txt') as whosThis:
    # Make array of elfs
    weAreElves = whosThis.read().split('\n\n');
    iHaveTheFood = []
    # Loop through each elf
    for elf in weAreElves :
        # Split the values for each elf
        elf = elf.split('\n')
        iHaveTheFood.append(sum(elf))

    # Get the highest value
    print('Most snacks:', max(iHaveTheFood))

    # Sort the array of calorie values
    weSortedAllTheFoods = sorted(iHaveTheFood)

    # Get top 3 values
    theBestThreeElves = weSortedAllTheFoods[-3 : ]

    print("Top {} values for snacks:".format(3), theBestThreeElves)

    # Get sum of top 3 values
    woopWeHaveMoreFood = sum(theBestThreeElves)

    print(woopWeHaveMoreFood)