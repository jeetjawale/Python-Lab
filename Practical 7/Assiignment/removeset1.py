set_a = set(input("Enter the elements of set A separated by spaces: "))
set_b = set(input("Enter the elements of set B separated by spaces: "))
intersection = set_a.intersection(set_b)
set_a -= intersection
print("The updated set_a is:", set_a)
