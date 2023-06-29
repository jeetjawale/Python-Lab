set_a = set(input("Enter the elements of set A separated by spaces: "))
set_b = set(input("Enter the elements of set B separated by spaces: "))
intersection = set_a.intersection(set_b)
symmetric_difference = set_a.symmetric_difference(set_b)
symmetric_difference = symmetric_difference - intersection
print("The elements present in set A or B but not both are:", symmetric_difference)
