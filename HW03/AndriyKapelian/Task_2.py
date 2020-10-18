number = input('Please enter four-digit number: ')
while not number.isdigit() or len(number) != 4:
    number = input('Please enter four-digit number: ')

# multiplication
result = 1
for item in number:
    item_to_int = int(item)
    result = result * item_to_int
print(result)

# reverse number
reversed_number = number[::-1]
print(reversed_number)

# sort number
sorted_number = sorted(number)
print("".join(sorted_number))