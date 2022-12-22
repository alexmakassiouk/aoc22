from math import sqrt
with open('9/input.txt') as f:
    lines = f.readlines()


class Knot:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.unique_locs = [str(self.x)+" "+str(self.y)]
    def move_knot(self, direction: chr):
        match direction:
            case 'D':
                self.y-=1
            case 'L':
                self.x-=1
            case 'U':
                self.y+=1
            case 'R':
                self.x+=1
        new_loc = str(self.x)+" "+str(self.y)
        if new_loc not in self.unique_locs:
            self.unique_locs.append(new_loc)

    def distance_to(self, other_knot):
        x_distance = abs(self.x-other_knot.x)
        y_distance = abs(self.y-other_knot.y)
        if self.is_diagonal(other_knot):
            distance = 1
        elif x_distance == 0 and y_distance == 0:
            distance = 0
        else:
            distance = sqrt(x_distance**2+y_distance**2)
        return distance
    def is_diagonal(self, other_knot):
        x_distance = abs(self.x-other_knot.x)
        y_distance = abs(self.y-other_knot.y)
        if x_distance == 1 and y_distance == 1:
            return True
        else:
            return False


head = Knot()
tail = Knot()

def main():
    for line in lines:
        direction = line.split(" ")[0]
        distance = int(line.split(" ")[1][:-1])

        for i in range(distance):
            prev_pos = str(head.x)+" "+str(head.y)
            head.move_knot(direction)
            if tail.distance_to(head) > 1:
                tail.x = int(prev_pos.split(" ")[0])
                tail.y = int(prev_pos.split(" ")[1])
                if prev_pos not in tail.unique_locs:
                    tail.unique_locs.append(prev_pos)
        # if tail.is_diagonal(head) and distance > 1:
        #     tail.x = head.x
        #     tail.y = head.y
        #     if str(tail.x)+str(tail.y) not in tail.unique_locs:
        #         tail.unique_locs.append(str(tail.x)+str(tail.y))
        # for i in range(distance+1):
        #     head.move_knot(direction)
        # if tail.distance_to(head) > 1:
        #     for i in range(distance):
        #         tail.move_knot(direction)
    print(len(tail.unique_locs))


def unit_test():
    head.move_knot('R', 5)
    head.move_knot('U', 3)
    head.move_knot('L', 5)
    head.move_knot('D', 3)
    head.move_knot('R', 5)
    tail.move_knot('R', 5)
    tail.move_knot('U', 3)
    print(head.distance_to(tail))
    print(head.unique_locs)

main()