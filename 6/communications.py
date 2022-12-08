with open('6/input.txt') as f:
    line = f.readline()

q = ""
i=0
for char in line:
    i+=1
    q+=char
    if len(q) >14:
        q = q[1:]
    if len(q) == 14 and len(set(q)) == 14:
        print(i)
        break