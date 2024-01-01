def multiply(*numbers):
   total = 1
   for number in numbers:
       total *= number
   return total
       
print(multiply(3, 4, 5, 6))

def addition(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(addition(4, 5, 6, 7))