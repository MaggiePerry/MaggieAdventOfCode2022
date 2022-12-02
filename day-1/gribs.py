import numpy as np

with open('day-1/input.txt') as whosThis:
    weAreElves = whosThis.read().split('\n\n');
    pleaseINeedFood = []
    for elf in weAreElves :
        elf = elf.split('\n')
        iHaveTheFood = 0
        for foods in elf :
            iHaveTheFood += int(foods)
            pleaseINeedFood.append(iHaveTheFood)
    iHaveTheMostFood = np.max(pleaseINeedFood)
    print(iHaveTheMostFood)
