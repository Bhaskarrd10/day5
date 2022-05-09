fruits = ["apple", "orange", "mango"]
for fruit in fruits:
  print(fruit)
print(fruits)


for number in range(1, 10):
  print(number)

total = 0
for number in range(1, 101):
  total += number
print(total)


for number in range(1, 101):
  if number % 3 == 0 and number % 5 ==0:
    print("FizzBuzz")
  elif number  % 5 == 0:
    print("Buzz")
  elif number % 3 == 0:
    print("Fizz")
  else:
    print(number)



    