with open('13/input.txt') as f:
    lines = f.readlines()

total = 0
for i in range(0, len(lines), 3):
    left = lines[i]
    right = lines[i+1]
    left = left[1:-1]
    right = right[1:-1]

    left_items = left.split(",")
    right_items = right.split(",")