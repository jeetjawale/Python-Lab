string = input("Enter a string: ")
characters = input("Enter the characters to find their frequency: ").split()
frequency = {}
for char in string:
    if char in characters:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print("Character frequencies:")
for char, count in frequency.items():
    print(char, "=", count)
