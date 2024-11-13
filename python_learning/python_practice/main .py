from datetime import datetime

# Name = input("What is your name?: ")
# Bday = input("Did you celebrate your birthday this year? (yes or no): ")
# Age = int(input("How old are you?: "))
# current_year = datetime.now().year

# celebration_year = current_year + (100 - Age)

# match Bday:
# case 'y' | 'yes' | 'yup'
# print("Congratulations!", Name, "you will turn 100 in: ", celebration_year)
# case 'n' | 'no' | 'nope'
# celebration_year = celebration_year - 1
# print( Name, "you will turn 100 in: ", celebration_year)
# case _:
# print("wrong statement")



name = input("What is your name: ")
age = int(input("How old are you: "))
year = 2024 - age + 100
print(name + ", you will be 100 years old in the year " + str(year))