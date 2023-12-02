'''

The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the
Elves now need to recover. On each line, the calibration value can be
found by combining the first digit and the last digit (in that order) 
to form a single two-digit number.

Consider your entire calibration document. What is the sum of all of
the calibration values?

'''

#read file
file = open("day_1/trebuchet_input.txt", "r")

sum = 0

for line in file:
    line = line.strip()
    l, r = 0, len(line) - 1

    while l < len(line) and not line[l].isdigit():
        l += 1
    while r > 0 and not line[r].isdigit(): 
        r -= 1

    sum += int(line[l] + line[r])

print(sum)
    
        

    

