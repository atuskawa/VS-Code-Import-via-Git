dataset = [24, 3, 60, 7, 9, 11]

#-----------------------------------------------Question 1 Ascending to Descending (No library)
for num1 in range(len(dataset) - 1):
    for num2 in range(len(dataset) - 1 - num1):
        if dataset[num2] > dataset[num2 + 1]:
            dataset[num2], dataset[num2 + 1] = dataset[num2 + 1], dataset[num2]

ascending = dataset[:]
descending = ascending[::-1] 

#(line 10 shows list slicing, it automatically reverses instead of arranging it all over again)

print("Ascending: ", ascending)
print("Descending: ", descending)

#-----------------------------------------------Question 2 odd and even counter
even_counter = 0; odd_counter = 0

for num in dataset:
    if num % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

print("Even counter: ", even_counter)
print("Odd counter: ", odd_counter)

#-----------------------------------------------Question 3 Sum of all elements
total_sum = 0
for num in dataset:
    total_sum += num
print ("Sum: ", total_sum)

