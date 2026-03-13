# pseudocode
# var initial = 5
# var total = 91
# var rate = 0.4
# var infected = initial
# while infected < total:
#     infected = infected + (infected * rate)
# add all infected to total and check whether it is greater than total
# if it is, break the loop and print the number of infected

initial = input("Enter the initial number of infected individuals: ")
total = input("Enter the total population: ")
rate = input("Enter the infection rate (as a decimal): ")

# default values for testing and transform the input values to the correct data types
initial = 5 if initial == "" else int(initial)
total = 91 if total == "" else int(total)
rate = 0.4 if rate == "" else float(rate)

day = 0
infected = initial
while infected < total:
    infected = infected + round(infected * rate, 0)  # round the number of infected to the nearest whole number
    day += 1    # count the number of days it takes for the infection to spread to the total population

print(f"The day to infect the total population is {day}")
