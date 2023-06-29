num_elements = int(input("Enter the number of elements for set 1: "))
elements1 = []
for i in range(num_elements):
    elements1.append(input("Enter element {} for set 1: ".format(i + 1)))
set1 = set(elements1)
num_elements = int(input("Enter the number of elements for set 2: "))
elements2 = []
for i in range(num_elements):
    elements2.append(input("Enter element {} for set 2: ".format(i + 1)))
set2 = set(elements2)
intersection = set1.intersection(set2)
print("The intersection of the two sets is:", intersection)
