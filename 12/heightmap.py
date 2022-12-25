from math import sqrt, inf
from bfs import bfs
from graph import Node, Graph

with open('12/input.txt') as f:
    lines = f.readlines()

dest = ""
start = ""
pos = ""
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "E":
            dest = str(i) + " " + str(j)
        if lines[i][j] == "S":
            start = str(i) + " " + str(j)
            pos = str(i) + " " + str(j)

print("Start: ", start)
print("Destination: ", dest)
distance = sqrt((int(dest.split(" ")[1])-int(pos.split(" ")[1]))**2 + (int(dest.split(" ")[0])-int(pos.split(" ")[0]))**2)
print("Distance:", distance)

def update_distance():
    global distance
    global dest
    global pos
    distance = sqrt((int(dest.split(" ")[1])-int(pos.split(" ")[1]))**2 + (int(dest.split(" ")[0])-int(pos.split(" ")[0]))**2)

# while pos!=dest:
#     y = int(pos.split(" ")[0])
#     x = int(pos.split(" ")[1])
#     elevation = lines[y][x]
#     if elevation =="S":
#         elevation = "a"
nodes = [[] for i in range(len(lines))] 
for i in range(len(lines)):
    for j in range(len(lines[i])):
        elevation = lines[i][j]
        if elevation == "S":
            elevation = "a"

        elif elevation == "E":
            elevation = "z"
        new_node = Node(j,i,elevation)
        nodes[i].append(new_node)
        if i == 20 and j == 0:
            start_node = new_node

height_map = Graph()

for row in nodes:
    for node in row:
        if node.y-1 >= 0:
            up = str(node.y-1) + " " + str(node.x)
            up_node = nodes[node.y-1][node.x]
        else:
            up = None
            up_node = None
        if node.y+1<40:
            down = str(node.y+1) + " " + str(node.x)
            down_node = nodes[node.y+1][node.x]
        else:
            down = None
            down_node = None
        if node.x-1 >= 0:
            left = str(node.y) + " " + str(node.x-1)
            left_node = nodes[node.y][node.x-1]
        else:
            left = None
            left_node = None
        if node.x+1 <= j:
            right = str(node.y) + " " + str(node.x+1)
            right_node = nodes[node.y][node.x+1]
        else:
            right = None
            right_node = None
        
        if up_node!=None and ord(up_node.elevation)-ord(node.elevation) <= 1:
            node.add_adj(up_node)
        if down_node!=None and ord(down_node.elevation)-ord(node.elevation) <= 1:
            node.add_adj(down_node)
        if left_node!=None and ord(left_node.elevation)-ord(node.elevation) <= 1:
            node.add_adj(left_node)
        if right_node!=None and ord(right_node.elevation)-ord(node.elevation) <= 1:
            node.add_adj(right_node)
        height_map.add_node(node)

bfs(height_map, start_node)
print("Completed")

#best_node = Node()
best_dist = inf
for row in nodes:
    for node in row:
        if node.elevation == "a" or node.elevation == "S":
            bfs(height_map, node)
            if nodes[20][148].key <best_dist:
                best_node = node
                best_dist = nodes[20][148].key
print(best_dist)