dataset = [24, 3, 60, 7, 9, 11]

#---------------------------------------------------Question 1 Ascending to Descending
ascending = sorted(dataset)
descending = sorted(dataset, reverse=True)

print("Ascending:", ascending)
print("Descending:", descending)

#---------------------------------------------------Question 2 Sort Odd and Even
even_count = sum (1 for x in dataset if x % 2 == 0)
odd_count = sum (1 for x in dataset if x % 2 != 0)

print("Even Count:", even_count)
print("Odd Count:", odd_count)

#---------------------------------------------------Question 3 Sum of all Numbers
total_sum = sum(dataset)

print("Sum:", total_sum)


