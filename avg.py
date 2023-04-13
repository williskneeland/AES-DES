import re

with open('./AES-Results.txt', 'r') as file:
    lines = file.readlines()

avg = 0
for line in lines:
    if '#' in line:
        print('\n\n')
        print('On', line)
    elif len(line) == 1:
        print(f'avg = {avg/5}ms')
        avg = 0
    else:
        avg += int(re.search('\d{3,4}(?=\D*$)', line).group())