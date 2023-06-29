import random
lst = [1, 1, 2, 3, 4, 4, 5, 1]
print("Original list:", lst)
num = int(input("Enter the number of randomly selected elements to extract: "))
selected_elements = random.sample(lst, num)
print("Selected elements:", selected_elements)