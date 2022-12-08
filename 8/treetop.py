with open('8/input.txt') as f:
    lines = f.readlines()
forest = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]

def setup_forest():
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            forest[i][j] = lines[i][j]
        del(forest[i][len(lines[i])-1])
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            forest[i][j] = int(forest[i][j])
    print("Forest setup complete")

def is_visible_left(tree_height: int, i: int, j: int):
    for k in range(j-1, -1, -1):
        if forest[i][k] >= tree_height:
            return is_visible_right(tree_height, i, j)
    return True
def is_visible_right(tree_height: int, i: int, j: int):
    for k in range(j+1, len(forest[i])):
        if forest[i][k] >= tree_height:
            return is_visible_top(tree_height, i, j)
    return True
def is_visible_top(tree_height: int, i: int, j: int):
    for k in range(i-1, -1, -1):
        if forest[k][j] >= tree_height:
            return is_visible_bottom(tree_height, i, j)
    return True
def is_visible_bottom(tree_height: int, i: int, j: int):
    for k in range(i+1, len(forest)):
        if forest[k][j] >= tree_height:
            return False
    return True

def main():
    setup_forest()
    visible_tree_count = 0
    
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            tree_height = int(forest[i][j])
            if is_visible_left(tree_height, i, j):
                visible_tree_count+=1
    print(visible_tree_count)

######## PART 2 #########

def viewing_distance_left(tree_height: int, i: int, j: int):
    viewing_distance = 0
    for k in range(j-1, -1, -1):
        viewing_distance+=1
        if forest[i][k] >= tree_height:
            return viewing_distance
    return viewing_distance
def viewing_distance_right(tree_height: int, i: int, j: int):
    viewing_distance = 0
    for k in range(j+1, len(forest[i])):
        viewing_distance+=1
        if forest[i][k] >= tree_height:
            return viewing_distance
    return viewing_distance
def viewing_distance_top(tree_height: int, i: int, j: int):
    viewing_distance = 0
    for k in range(i-1, -1, -1):
        viewing_distance+=1
        if forest[k][j] >= tree_height:
            return viewing_distance
    return viewing_distance
def viewing_distance_bottom(tree_height: int, i: int, j: int):
    viewing_distance = 0
    for k in range(i+1, len(forest)):
        viewing_distance+=1
        if forest[k][j] >= tree_height:
            return viewing_distance
    return viewing_distance

def main2():
    setup_forest()
    scenic_scores = []

    for i in range(len(forest)):
        for j in range(len(forest[i])):
            tree_height = int(forest[i][j])
            scenic_scores.append(viewing_distance_left(tree_height, i, j)*viewing_distance_right(tree_height, i, j)*viewing_distance_top(tree_height, i, j)*viewing_distance_bottom(tree_height, i, j))
            
    print(max(scenic_scores))
main2()