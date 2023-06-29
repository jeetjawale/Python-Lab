lst = [1, 1, 2, 3, 4, 4, 5, 1]
print("Given list:", lst)
elem = int(input("Enter the element to be inserted: "))
pos = int(input("Enter the position at which the element is to be inserted: "))
lst.insert(pos, elem)
print("Modified list:",lst)