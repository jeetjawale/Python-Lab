set_a = set(input("Enter the elements of set A separated by spaces: "))
set_b = set(input("Enter the elements of set B separated by spaces: "))
if set_a.intersection(set_b):
    print("The common elements are:", set_a.intersection(set_b))
else:
    print("The two sets have no common elements.")
