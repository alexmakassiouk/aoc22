with open('7/input.txt') as f:
    lines = f.readlines()

global path
path = ""
global active_directory
active_directory = ""


def cd(directory: str):
    global path
    global active_directory
    if directory == "..":
        newPath = '/'.join(str(e) for e in path.split("/")[:-2]) + "/"
        active_directory = newPath.split("/")[-2]
    elif directory == "/":
        newPath = "/"
        active_directory = "/"
    else:
        newPath = path+directory+"/"
        active_directory = directory.split("/")[-1]
    path = newPath

def unit_test_cd():
    global path
    path+="/mappe1/mappe2/halla/"
    cd("..")
    cd("..")
    cd("hehe/skjera")
    print(path)

def main():
    global path
    global active_directory
    known_directories = {"/": 0}
    for line in lines:
        line_elements = line[:-1].split(" ")
        if line_elements[0] == "$" and line_elements[1] == "cd":
            new_dir = line_elements[2]
            cd(new_dir)
            if new_dir not in known_directories:
                known_directories[new_dir] = 0
        if line_elements[0] == "dir" and line_elements[1] not in known_directories:
            known_directories[line_elements[1]] = 0
        if line_elements[0].isdigit():
            size = int(line_elements[0])
            #known_directories.update({active_directory:known_directories[active_directory]+size})
            if path!="/":
                ancestors = path.split("/")
                ancestors.append("/")
                for parent in ancestors:
                    if parent!="":
                        known_directories.update({parent:known_directories[parent]+size})
    total = 0
    for x in known_directories:
        print(x, known_directories.get(x))
    for directory in known_directories.values():
        if directory<=100000:
            total+=directory
    print(total)

main()