# def greet():
  # print("Hello")
  # print("how do you do")

# greet()

# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"What is it like in {location}")

# greet_with("Jack Bauer", "Nowhere")

# import math

# def paint_calc(height, width, cover):
#   area = height * width
#   num_of_cans = math.ceil(area / cover)
#   print(f"You'll need {num_of_cans} cans of paint")

def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("prime")
  else:
    print("not prime")
