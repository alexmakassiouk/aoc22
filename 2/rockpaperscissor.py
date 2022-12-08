with open('2/input.txt') as f:
    lines = f.readlines()

def get_result(game: str):
    opponent = game.split(" ")[0]
    player = game.split(" ")[1][0]
    if (opponent == "A" and player == "Y") or (opponent == "B" and player == "Z") or (opponent == "C" and player == "X"):
        return "W"
    elif (opponent == "A" and player == "Z") or (opponent == "B" and player == "X") or (opponent == "C" and player == "Y"):
        return "L"
    else:
        return "D"

def get_result2(game: str):
    res = game.split(" ")[1][0]
    if res == "X":
        return "L"
    elif res == "Y":
        return "D"
    else:
        return "W"

def get_score(result: chr, weapon:chr):
    weapon_score = 0
    result_score = 0
    if weapon == "X":
        weapon_score = 1
    elif weapon == "Y":
        weapon_score = 2
    else:
        weapon_score = 3
    if result == "W":
        result_score = 6
    elif result == "D":
        result_score = 3
    else:
        result_score = 0
    return weapon_score+result_score

def part_1():
    summen = 0
    for line in lines:
        res = get_result(line)
        summen+=get_score(res, line.split(" ")[1][0])
    print(summen)

def find_contestant(opponent: chr, result: chr):
    if result == "D":
        if opponent == "A":
            contestant = "X"
        elif opponent == "B":
            contestant = "Y"
        else:
            contestant = "Z"
    elif result == "W":
        if opponent == "A":
            contestant = "Y"
        elif opponent == "B":
            contestant = "Z"
        else:
            contestant = "X"
    else:
        if opponent == "A":
            contestant = "Z"
        elif opponent == "B":
            contestant = "X"
        else:
            contestant = "Y"
    return contestant

def part_2():
    summen = 0
    for line in lines:
        res = get_result2(line)
        contestant = find_contestant(line.split(" ")[0], res)
        summen+=get_score(res, contestant)
    print(summen)
part_2()