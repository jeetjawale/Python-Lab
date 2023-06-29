first_set = set(input("Enter the elements of the first set: "))
second_set = set(input("Enter the elements of the second set: "))
first_set.difference_update(second_set)
print("The updated first set is:", first_set)
