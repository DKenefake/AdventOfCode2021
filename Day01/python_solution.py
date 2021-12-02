###################
# Problem 1 Part 1
###################

# open the file with the depth inputs
file = open('input.txt', 'r')

# read in the file line by line and conver to integers
lines = [int(line.rstrip()) for line in file.readlines()]

# closing IO resources is a good idea
file.close()

# lambda that counts the instances when the depth gets lower
counter = lambda x: x[1] > x[0] > 0

# apply the counter to the depth data and sum the results
sol_1_1 = sum(map(counter, zip(lines, lines[1:])))

# display the solution
print(f'The solution to P1P1 is {sol_1_1}')


##################
#Problem 1 Part 2
##################

# take moving sum of depth data
average = [sum(measures) for measures in zip(lines, lines[1:], lines[2:])]

# apply counter to the depth data and sum the results
sol_1_2 = sum(map(counter, zip(average, average[1:])))

# display the solution
print(f'The solution to P1P2 is {sol_1_2}')
