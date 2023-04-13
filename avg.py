import re

with open('./AES-Results.txt', 'r') as file:
    lines = file.readlines()

avg = 0
for line in lines:
    if '#' in line:
        print('On', line)
    elif '/' in line:
        print(f'avg = {avg/5}ms')
        avg = 0
    else:
        print(re.search('^.*TIME.*([0-9]*).ms$', line))