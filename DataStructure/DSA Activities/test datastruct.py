dataset = [24, 3, 60, 7, 9, 11]

for num1 in range(len(dataset) - 1):
    for num2 in range(len(dataset) - 1 - num1):
        if dataset[num2] > dataset[num2 + 1]:
            dataset[num2], dataset[num2 + 1] = dataset[num2 + 1], dataset[num2]

ascending = dataset[:]
descending = ascending[::-1] #big brain list slicing wtf? (automatically reverses instead of arranging it all over again)

print("Ascending: ", ascending)
print("Descending: ", descending)

#Note: More efficient version.


#------------------------------------------------------------------------------------------------

dataset = [24, 3, 60, 7, 9, 11]
for num1 in range(len(dataset) - 1):
    for num2 in range(len(dataset) - 1 - num1):
        if dataset[num2] > dataset[num2 + 1]:
            dataset[num2], dataset[num2 + 1] = dataset[num2 + 1], dataset[num2]

acsending = dataset[:]
print("Ascending: ", dataset)

for num1 in range(len(dataset) - 1):
    for num2 in range(len(dataset) - 1 - num1):
        if dataset[num2] < dataset[num2 + 1]:
            dataset[num2], dataset[num2 + 1] = dataset[num2 + 1], dataset[num2]

descending = dataset[:]
print("Descending: ", dataset)

#Note: Slow as fuck dude