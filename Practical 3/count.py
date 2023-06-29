string = "P@#yn26at^&i5ve"
letter_count = 0
digit_count = 0
special_count = 0
for char in string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1
print("Letter count:", letter_count)
print("Digit count:", digit_count)
print("Special symbol count:", special_count)
