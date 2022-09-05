whole_number = int(input("Kokonaisluku"))
numbers_list = [9, 8, 7, 6, 5, 4, 3, 2]
is_prime = False

if whole_number / whole_number == 1 and whole_number / 1 == whole_number:
    is_prime = True

for number in numbers_list:
   if whole_number % number == 0:
       is_prime = False


if is_prime == True:
    print(f"Number {whole_number} is a prime number")
else:
    print(f"Number {whole_number} is not a prime number")

