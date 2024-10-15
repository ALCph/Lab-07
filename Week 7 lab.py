#1.)
# Weekly sales problem
sales = [] # Making an empty list to append stuff too
# Setting up the while loop
count = 0
while count < 7:
    value = float(input('Enter the sales for this day: '))
    sales.append(value)
    count+=1
# Printing the output
print(f'The total sales for the week is ${sum(sales):.2f}.')
#------------------------------------------------------------------------

#2.)
# Lottery and random numbers
import random
ticket = [0] * 7 # Making a list with 7 empty values that will be replaced

# The for loop
for i in range(7):
    ticket[i] = random.randint(0, 9)
    
# Printing the output
print(ticket)
#------------------------------------------------------------------------

#3.)
# Rainfall measuring
# An empty list that we will use for appending
rainfall = []
# User inputs
for i in range(1, 13):
    monthly_rain = float(input('Enter the rainfall for this month: '))
    rainfall.append(monthly_rain)

# Some calculations and new variables
total_rain = sum(rainfall)
average_rain = total_rain / 12

highest_rainfall = max(rainfall)
lowest_rainfall = min(rainfall)

# Variables for getting the months with the min and max rain. Solely for the print statement
month_highest = rainfall.index(highest_rainfall) + 1
month_lowest = rainfall.index(lowest_rainfall) + 1

# Printing the output
print(f'The total amount of rainfall this year was {total_rain:.2f} inches')
print(f'The average amount of rainfall this year was {average_rain:.2f} inches')
print(f'Month with highest rainfall: Month {month_highest} ({highest_rainfall:.2f} inches)')
print(f'Month with lowest rainfall: Month {month_lowest} ({lowest_rainfall:.2f} inches)')
#------------------------------------------------------------------------

#4.)
# A problem involving a big list
big_list = [] #empty list for appending
count = 0

# Using a while loop for this one
while count < 20:
    number = int(input('Enter a number: '))
    big_list.append(number)
    count+=1

# One final calculation before printing
avg = sum(big_list) / len(big_list)

# Printing the output
print(f'Lowest number on the list: {min(big_list)}')
print(f'Highest number on the list: {max(big_list)}')
print(f'Sum for numbers on the list: {sum(big_list)}')
print(f'Average for numbers on the list: {avg}')
#------------------------------------------------------------------------

#5.)
# Charge account validation
# Opening the file as read, and then removing the /n character
with open('charge_accounts.txt', 'r') as file:
    accounts = [line.rstrip() for line in file] #I had to get a refresher on that line.rstrip command 

# User input
account_number = int(input('Enter the account number: '))

# Comparing account numbers and printing the output
if account_number in accounts:
    print('The account number is valid')
else:
    print('The account number is invalid')
#------------------------------------------------------------------------

#6.)
# Lists and arguments

#Sample data used for testing
numbers = [5, 10, 15, 20, 25, 30]
n = 1
# The function
def Larger_than(list_numbers, n):
    for number in list_numbers:
        if number > n:
            print(number)

#Calling the function
Larger_than(numbers, n)
#------------------------------------------------------------------------

#7.)
# Driver test questions

# Correct answers list
correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

# I made and used a .txt file when testing this
# Still dont quite have the handle on commands to strip /n. Struggled here
with open('student_answers.txt', 'r') as file:
    student_answers = file.read().splitlines()

# Counters that we will modifying
correct_count = 0
incorrect_count = 0
incorrect_questions = []

# Comparing the answers
for i in range(len(correct_answers)):
    if student_answers[i] == correct_answers[i]:
        correct_count += 1
    else:
        incorrect_count += 1
        incorrect_questions.append(i + 1) 

# Printing the output
if correct_count >= 15:
    print("You passed the exam.")
else:
    print("You failed the exam.")

print(f'Total correct: {correct_count}')
print(f'Total incorrect: {incorrect_count}')
print(f'Questions that were incorrect:, {incorrect_questions}')
#------------------------------------------------------------------------

#8.)
# Popular names
# Very similar to problem #5? So I just reused the code

# Opening the file as read, and then removing the /n character when assigning it to a variable
with open('popular_names.txt', 'r') as file:
    pop_names = [line.rstrip() for line in file] 

# User input
name_search = (input('Enter a name to search: '))

# Comparing names and the print message
if name_search in pop_names:
    print('This name is very popular')
else:
    print('This name is not very popular')
#------------------------------------------------------------------------

#9.)
# Counting the population
# An empty list that will be filled with info from the USPopulation.txt
population = []

# Opening the .txt file and appending the empty list above with the year info
with open('USPopulation.txt', 'r') as file:
    for line in file:
        population.append(int(line.strip()))

# Counter variables
total_change = 0
annual_changes = []
# Appending the list with changes in population
for i in range(1, len(population)):
    change = population[i] - population[i - 1]
    annual_changes.append(change)
    total_change += change

# Average annual change
average_change = total_change / (len(population) - 1)

# Sorting the info
# Adding 1951 to the calculation to get the year is something that took me a bit
max_grouth = max(annual_changes)
min_growth = min(annual_changes)
year_max_grouth = annual_changes.index(max_grouth) + 1951  
year_min_growth = annual_changes.index(min_growth) + 1951 

# Printing the output
print(f'Average annual change in population: {average_change:.2f} thousand')
print(f'Year with greatest increase in population: {year_max_grouth}')
print(f'Year with smallest increase in population: {year_min_growth}')
#------------------------------------------------------------------------

#10.)
# World series winners
# Opening the file to read
with open('WorldSeriesWinners.txt', 'r') as file:
    winners = file.readlines()

# A command to strip the newline character
winners = [team.strip() for team in winners]

# Getting the team name from the user and the count
team_name = input("Enter the name of the team: ")
win_count = winners.count(team_name)

# Printing the output
print(f"{team_name} has won the World Series {win_count} times from 1903 to 2009.")
