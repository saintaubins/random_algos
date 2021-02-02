from random import *

rand = random()  # gets a number between 0.0 and 1.0

print(rand)

rand =  50 + random() * 200      # gets a number between 50 and 250

print(rand)

rand  = uniform(50, 250)  # gets a number between 50 and 250

print(rand)

outcomes = ['win', 'lose', 'double', 'triple', 'try again' ]

rand_outcome = choice(outcomes)  # this gets a random choice

print(rand_outcome)

rand_outcomes = choices(outcomes, k=10) # this prints 10 random choices

print(rand_outcomes)