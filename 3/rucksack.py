with open('3/input.txt') as f:
    lines = f.readlines()

def find_common_item(contents: str):
    n = len(contents)-1
    mid = int(n/2)
    sub1 = contents[:mid]
    sub2 = contents[mid:-1]
    common_item = ""
    for item1 in sub1:
        for item2 in sub2:
            if item1 == item2:
                common_item = item1
                return common_item

def find_common_badge(elf1: str, elf2: str, elf3: str):
    common_item = ""
    for item1 in elf1:
        for item2 in elf2:
            for item3 in elf3:
                if item1 == item2 == item3:
                    common_item = item1
                    return common_item
    print("fail: ",common_item)

def find_priority(item):
    items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return items.index(item)+1

def find_badge():
    elves = []
    total = 0
    i = 0
    for line in lines:
        if len(elves) == 3:
            total+=find_priority(find_common_badge(elves[0][:-1], elves[1][:-1], elves[2][:-1]))
            print(i, ":", find_priority(find_common_badge(elves[0][:-1], elves[1][:-1], elves[2][:-1])))
            elves = [line]
        else:
            elves.append(line)
        i+=1
    print(i, total)

    total+= find_priority(find_common_badge("nPPssTBnMJPdtHPVHtRhpv", "bSSgGFWDgWwDFFlmWlcShqdpRqpVcHvvnqpvpRHd", "bGFnGljgSsjBCTBszz"))
    print(total)

def find_total_priority():
    total = 0
    for line in lines:
        total+=find_priority(find_common_item(line))
    print(total)



find_badge()