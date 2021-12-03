###################
# Problem 2 Part 1
###################

from dataclasses import dataclass

# open the file with the depth inputs
file = open('input.txt', 'r')
   
# read in the file line by line and conver to integers
commands = [line.rstrip().split() for line in file.readlines()]

# close IO resources
file.close()

def parse_command(command):
    """
    Parse a command for forward/down/up into a dict giving directions
    """
    command_type = command[0]
    command_amount = int(command[1])
    
    operations = {'forward':0, 'down':0, 'up':0, }
    
    operations[command_type] += command_amount
    
    return operations 
  
# create a class for the submarine
@dataclass
class SubState:
    horizontal : int = 0
    vertical : int = 0
    aim: int = 0
        
    def take_move(self, move:dict, rule):
        rule(self, move)

        
# our move rule set for subproblem 1
def rule_1(sub, move):
    sub.horizontal += move['forward']
    sub.vertical -= move['up']
    sub.vertical += move['down']

# make a new sub
submarine = SubState()

# apply all of the commands to the sub
for move in map(parse_command, commands):
    submarine.take_move(move, rule_1)
    
print(f'The solution to problem 2 part 1 is {submarine.horizontal * submarine.vertical}')

###################
# Problem 2 Part 2
###################

# our move set rule for subproblem 2
def rule_2(sub, move):
    sub.aim += move['down']
    sub.aim -= move['up']
    
    sub.horizontal += move['forward']
    sub.vertical += sub.aim * move['forward']

# make a new sub
submarine = SubState()

# apply all of the commands to the sub
for move in map(parse_command, commands):
    submarine.take_move(move, rule_2)
    
print(f'The solution to problem 2 part 2 is {submarine.horizontal * submarine.vertical}')
