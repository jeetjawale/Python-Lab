num_elements = int(input("Enter the number of elements: "))
elements = []
for i in range(num_elements):
    elements.append(input("Enter element {}: ".format(i + 1)))
set_elements = set()
for element in elements:
    set_elements.add(element)
print(set_elements)
