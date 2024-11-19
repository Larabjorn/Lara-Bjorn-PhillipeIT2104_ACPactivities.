def is_perfect_number(number):
    if number <= 0:
        return False

    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        num = int(user_input)
        if is_perfect_number(num):
            print(f"{num} is a perfect number.")
        else:
            print(f"{num} is not a perfect number.")
        break
    else:
        print("Please enter a valid integer.")
