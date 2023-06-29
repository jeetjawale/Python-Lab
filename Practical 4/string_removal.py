lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Given list:", lst)
indices_to_remove = [0, 4, 5]
for i in sorted(indices_to_remove, reverse=True):
    del lst[i]
print("List after removing specified elements:",lst)