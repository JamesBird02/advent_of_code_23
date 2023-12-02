'''
Your calculation isn't quite right. It looks like some of the digits are
actually spelled out with letters: one, two, three, four, five, six, seven,
eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first
and last digit on each line.

'''

#read file
file = open("day_1/trebuchet_input.txt", "r")

sum = 0

#text is all lower 

nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six':6, 'seven': 7, 'eight': 8,
        'nine': 9}


for line in file:
    line.strip()
    print(line)
    temp = []
