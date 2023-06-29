string = "PYnative29@#8496"  # You can modify the string here
digits = []
for char in string:
    if char.isdigit():
        digits.append(int(char))
digit_sum = sum(digits)
digit_average = digit_sum / len(digits)
print("Digits:", digits)
print("Sum of digits:", digit_sum)
print("Average of digits:", digit_average)
