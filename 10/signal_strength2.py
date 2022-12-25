with open('10/input.txt') as f:
    lines = f.readlines()
clk = 0
register = 1
signal_strengths = 0
display_lines = ["", "", "", "", "", ""]

def tick():
    global clk
    global signal_strengths
    global register
    if register-1 <= clk%40 <= register+1:
        display_lines[clk//40]+="#"
    else:
        display_lines[clk//40]+="."
    clk+=1
    if (clk-20)%40 == 0 and clk <= 220:
        signal_strengths+=clk*register

def addx(value):
    global register
    tick()
    tick()
    register+=value

def noop():
    tick()

def main():
    for line in lines:
        if line == "noop\n":
            noop()
        else:
            if int(line.split(" ")[1][0] == "-"):
                value = 1 * int(line.split(" ")[1][:-1])
            else:
                value = int(line.split(" ")[1][:-1])
            addx(value)

    print("Completed: ", signal_strengths)
    for line in display_lines:
        print(line)

main()