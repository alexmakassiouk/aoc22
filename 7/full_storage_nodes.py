with open('7/input.txt') as f:
    lines = f.readlines()

class Node:
    def __init__(self, value: int, name: str) -> None:
        self.value = value
        self.name = name
        self.parent = None
        self.children = []

root = Node(0, "/")

def main():
    known_nodes = {root.name: root}
    active_node = root
    leaves = []
    for line in lines:
        line_elements = line[:-1].split(" ")
        if line_elements[0] == "$" and line_elements[1] == "cd":
            if line_elements[2] == "..":
                active_node = active_node.parent
            elif line_elements[2] == "/":
                active_node = root
            else:
                new_node = Node(0,active_node.name+'/'+line_elements[2])
                new_node.parent = active_node
                active_node.children.append(new_node)
                active_node = new_node
                if new_node.name not in known_nodes:
                    known_nodes[new_node.name] = new_node
        elif line_elements[0] == "dir" and active_node.name+'/'+line_elements[1] not in known_nodes.keys():
            new_node = Node(0, active_node.name+'/'+line_elements[1])
            new_node.parent = active_node
            active_node.children.append(new_node)
            known_nodes[new_node.name] = new_node
        elif line_elements[0].isdigit():
            size = int(line_elements[0])
            new_node = Node(size, active_node.name+'/'+line_elements[1])
            new_node.parent = active_node
            active_node.children.append(new_node)
            leaves.append(new_node)
        #else:
            #print("Error:", line_elements)

    print("Completed tree init")

    folders = []
    for leaf in leaves:
        ancestor = leaf.parent
        while ancestor!=None:
            if ancestor not in folders:
                folders.append(ancestor)
            ancestor.value+=leaf.value
            ancestor = ancestor.parent
    print("Value updates complete")

    total = 0
    for folder in folders:
        if folder.value<=100000 and folder.value>0:
            total+=folder.value
    print(total)

    space_to_free = 70000000-root.value
    print(space_to_free)
    appropriate_folders = []
    for folder in folders:
        if folder.value >= 30000000-space_to_free:
            appropriate_folders.append(folder.value)
    print("Slett:", min(appropriate_folders))
main()