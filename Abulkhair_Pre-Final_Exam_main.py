def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


while True:
    start = int(input("Enter the starting number : "))

    if start < 0:
        print("Enter a non-negative number.")
        continue

    end = int(input("Enter the ending number: "))

    if end <= start:
        print(f"Enter a number greater than {start}.")
        continue

    if start == 0 or end == 0:
        print("Program terminated.")
        break

    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

    while True:
        user_input = int(input("Enter a number : "))

        if user_input == 0:
            print("Program terminated.")
        break