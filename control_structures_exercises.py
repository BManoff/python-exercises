#1.) Conditional Basics
#a.) prompt the user for a day of the week, print out whether the day is Monday or not
is_it_monday = input("Enter the day of the week Monday-Friday: ").lower()
if is_it_monday == 'Monday':
    print("It is Monday")
else:
    print("It is not Monday")

#b.) prompt the user for a day of the week, print out whether the day is a weekday or a weekend
weekday_or_weekend = input("Enter the day of the week Monday-Sunday: ").lower()
if weekday_or_weekend == ('Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday'):
    print("It is a weekday")
else:
    print("It is the weekend")

#c.) 
def paycheck(hours, pay):
    if hours > 40:
        return 40 * pay + (hours - 40) * pay * 1.5
    else: return hours * pay
print(paycheck(60,20))

#2.) loop basics
#a.) while
i = 5
while i <= 15:
    print(i)
    i += 1

i = 0
while i <= 100:
    print(i)
    i += 2

i = 100
while i >= -10:
    print(i)
    i -= 5

i = 2
while i <= 1000000:
    print(i)
    i = i**2

i = 100
while i >= 5:
    print(i)
    i -= 5

#b.) For Loops
#i.) Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.
multiply = int(input("Multiply this number by 10: "))
for i in range(1, 11):
    print(f"{multiply} x {i} = {multiply * i}")

#ii.)
for i in range(1,10):
    print(str(i) * i)

#c.) 
while True:
    if odd_number.isdigit():
        odd_number = int(odd_number)
        if odd_number % 2 == 0:
            continue
        break

i = 1
while i <= 50:
    if i == odd_number:
        print(f"Yikes! Skipping number: {i}")
        i += 2
        continue
    print(f"Here is an odd number: {i}")
    i += 2

 #d.)
while True:
    positive_number = input("Enter a positive number: ")
    if positive_number.isdigit():
        positive_number = int(positive_number)
        if positive_number <= 0:
            continue
        break

for i in range(0, positive_number + 1):
    print(i)

#e.)
while True:
    countdown = input("Please enter a positive number: ")
    if countdown.isdigit():
        countdown = int(countdown)
        if countdown <= 0:
            continue
        break

for i in range(countdown, 0, -1):
    print(i)

#3.)
i = 1
while i <= 100:
    print(i)
    i += 1

for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

#4.)
number_to_power = int(input("What number would you like to go up to?: "))

print()
print("number | squared | cubed")
print("-----  |  ----   | ----")
for i in range(1, number_to_power + 1):
    print("%6d | %7d | %5d" % (i, i**2, i**3))


#5.)
numerical_grade = int(input("Enter a grade number 1-100: "))
if numerical_grade >= 88:
    print("A")
elif numerical_grade >= 80:
    print("B")
elif numerical_grade >= 67:
    print("C")
elif numerical_grade >= 60:
    print("D")
else:
    print("F")

will_continue = input("Do you want to continue? ")
if will_continue.lower().startswith("y"):
    continue
break

#6.)
book_list = [
            {"title": "The Hobbit", 
            "author": "J. R. R. Tolkien", 
            "genre": "high fantasy"},

            {"title": "Harry Potter and the Goblet of Fire", 
            "author": "J. K. Rowling", 
            "genre": "fantasy"},

            {"title": "Ender's Game", 
            "author": "Orson Scott Card", 
            "genre": "science fiction"},
]

enter_genre = input("Enter a book genre for recommendation: ")
[book["title"] for book in book_list if book["genre"].lower() == enter_genre]
