num = int(input("Enter a number: "))
print("Table is", num)
for i in range(1, 11):
    result = num * i
    print(num, "x", i, "=", result)
