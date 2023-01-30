import re
tot=0
tot_l=[]
file = open('actual_data.txt')
for line in file:
    #line = line.rstrip()
    x = re.findall('([0-9]+)',line)
    if len(x) > 0:
        for i in x:
            tot_l.append(i)
for i in tot_l:
    tot += int(i)
print(tot)