string = "PyNaTive"
lowercase = []
uppercase = []
for char in string:
    if char.islower():
        lowercase.append(char)
    else:
        uppercase.append(char)
arranged_string = ''.join(lowercase + uppercase)
print("Arranged string:", arranged_string)
