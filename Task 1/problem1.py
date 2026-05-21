numbers = input("Enter numbers separated by spaces: ").split()

if len(numbers) == 0:
    print(-1)
else:
    numbers = list(map(int, numbers))
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        print(-1)
    else:
        unique_numbers.sort(reverse=True)
        print(unique_numbers[1])
