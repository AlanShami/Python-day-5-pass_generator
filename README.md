##Day-5_of_Python-PassGenerator

Credit: [Angela Yu] https://www.udemy.com/share/101Xwi3@Cd5H-edT3Ktu-_5Z3i14xX7vfWAqQSqiDCRRkMUqlu0NXefLQnWpT9ksckT6u1rs-g==/

This is day 5 of 100 of learning Python and creating a project in Python

10/18/2023

![](https://github.com/AlanShami/Python-day-5-pass_generator/blob/main/project_pic.png)

- [main.py](https://github.com/AlanShami/Python-day-5-pass_generator/blob/main/main.py)


#Comments:
Loops, for loop, while loop
 ----------------------------------------

fruits = ["apples", "Bananas", ]

for x in fruits:
   print(x)

 target = int(input())  # Enter a number between 0 and 1000

 total = 0

 for number in range(target + 1):
     if number % 2 == 0:
         total += number

 print(total)

 for number in range(101):
     if number % 5 == 0 & number % 3 == 0:
         print("FizzBuzz")
    elif number % 5 == 0:
        print("Fizz")
    elif number % 3 == 0:
         print("Buzz")
     else:
         print(number)


----------------------------------

print("alan"[5])

print(type(int("4")))
print(round(123.2323,2))

