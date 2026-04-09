# What does this piece of code do?
# Answer: It draws 11 random integers between 1 and 10 and prints their sum.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0
progress=0
while progress<=10:	# draw 10 random numbers
	progress+=1
	n = randint(1,10)	# randomly draw an integer between 1 and 10
	total_rand+=n	# add the random number one by one to the total

print(total_rand)

