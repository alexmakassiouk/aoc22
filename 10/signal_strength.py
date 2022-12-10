with open('10/example.txt') as f:
    lines = f.readlines()

line_index = 0
register = 1
# for i in range(1,1000):
#     if lines[line_index] == "noop\n":
#         line_index+=1
#     else:
#         if int(lines[line_index].split(" ")[1][0] == "-"):
#             value = 1* int(lines[line_index].split(" ")[1][:-1])
#         else:
#             value = int(lines[line_index].split(" ")[1][:-1])
#         i+=2
#         register+=value
#         line_index+=1
    
clock = 1
total = 0
for line in lines:
    if clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220:
        print(clock*register)
        total+=(clock*register)
    if line == "noop\n":
        clock+=1
    else:
        if int(line.split(" ")[1][0] == "-"):
            value = 1 * int(line.split(" ")[1][:-1])
        else:
            value = int(line.split(" ")[1][:-1])
        clock+=2
        register+=value
print("Completed")
print("Signal strengths: ", total)