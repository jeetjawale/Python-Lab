set_elements = set(input("Enter the set elements separated by spaces: "))
items_to_remove = input("Enter the items to remove separated by spaces: ").split()
for item in items_to_remove:
    set_elements.remove(item)
print("The updated set is:", set_elements)
