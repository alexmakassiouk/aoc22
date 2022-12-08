with open('1/input.txt') as f:
    lines = f.readlines()

elves = []
summen = 0
for line in lines:
    if line!="\n":
        summen+=int(line)
    else:
        elves.append(summen)
        summen = 0

top3 = []
for i in range(3):
    elf = max(elves)
    top3.append(elf)
    elves.remove(elf)
print(top3)
print(sum(top3))