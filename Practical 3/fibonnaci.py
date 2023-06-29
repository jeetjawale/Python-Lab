num = int(input("Enter a number: "))
def generate_fibonacci(n):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
fibonacci_sequence = generate_fibonacci(num)
print("Fibonacci sequence up to", num, ":")
for number in fibonacci_sequence:
    print(number)
