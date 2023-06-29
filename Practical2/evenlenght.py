num_strings = int(input("Enter the number of strings: "))
strings = []
even_length_strings = []
for i in range(num_strings):
    string = input("Enter a string: ")
    strings.append(string)
for string in strings:
    if len(string) % 2 == 0:
        even_length_strings.append(string)
print("Strings with even length:")
for string in even_length_strings:
    print(string)
