import re

file = open('regex_sum_19916.txt')
total = None
for line in file :
    numbers = re.findall('[0-9]+', line)
    for n in numbers :
        n = int(n)
        if total is None :
            total = n
            continue

        total += n

print(total)
