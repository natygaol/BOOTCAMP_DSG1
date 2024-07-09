def get_evens(numbers):
  evens = []
  for number in numbers:
    if number % 2 == 0:
      evens.append(number)
  return evens


numbers = [-1, 70, 3, 76, 99, 2, 7, 20, 66, 550]
evens = get_evens(numbers)
print(evens)


#list comprehensions

pairs = [number for number in numbers if number % 2 == 0]
print(pairs)