def find_max_and_min():
    numbers = []

    for i in range(1, 6):
        number = int(input(f"Ingrese el {i}° número: "))
        numbers.append(number)

    max_number = max(numbers)
    min_number = min(numbers)

    return max_number, min_number

max, min = find_max_and_min()

print(f"El número mayor es: {max}")
print(f"El número menor es: {min}")