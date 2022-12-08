with open('4/input.txt') as f:
    lines = f.readlines()

def separate_pair(line: str):
    first_elf, second_elf = line.split(",")
    return first_elf, second_elf

def get_start_stop(elf: str):
    start = int(elf.split("-")[0])
    stop = int(elf.split("-")[1])
    return [start, stop]

def is_fully_enclosed(elf1, elf2):
    # if elf1[0] >= elf2[0]:
    #     enclosed_elf = elf1
    #     hard_working_elf = elf2
    # else:
    #     enclosed_elf = elf2
    #     hard_working_elf = elf1

    # if enclosed_elf[1]<=hard_working_elf[1]:
    #     return True
    # else:
    #     return False
    if (elf1[0] >= elf2[0] and elf1[1]<=elf2[1]) or (elf2[0] >= elf1[0] and elf2[1] <= elf1[1]):
        return True
    else:
        return False

def overlaps(elf1, elf2):
    if (elf1[0]>= elf2[0] and elf1[0]<= elf2[1]) or (elf2[0] >= elf1[0] and elf2[0] <= elf1[1]):
        return True
    else:
        return False
    

def main1():
    total = 0
    for line in lines:
        elf1, elf2 = separate_pair(line)
        if is_fully_enclosed(get_start_stop(elf1), get_start_stop(elf2)):
            total+=1
    return total

print(main1())

def main2():
    total = 0
    for line in lines:
        elf1, elf2 = separate_pair(line)
        if overlaps(get_start_stop(elf1), get_start_stop(elf2)):
            total+=1
    return total

print(main2())