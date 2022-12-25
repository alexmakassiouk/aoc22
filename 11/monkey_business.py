class Monkey:
    def __init__(self, name, starting_items, operator, operand, test_operand, true_monkey, false_monkey) -> None:
        self.name = name
        self.items = starting_items
        self.operator = operator
        self.operand = operand
        self.test_operand = test_operand
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspect_item_count = 0

    def inspect_item(self):
        item = self.operate(self.items.pop(0))
        #item = item//3
        if item>=7*2*19*3*13*11*5*17:
            item = item % (7*2*19*3*13*11*5*17)
        self.inspect_item_count+=1
        if item%self.test_operand==0:
            return self.true_monkey, item
        else:
            return self.false_monkey, item

    def operate(self,item):
        if self.operator == "*":
            item = item*self.operand
        elif self.operator == "+":
            item = item+self.operand
        elif self.operator == "**":
            item = item**2
        return item


m0 = Monkey(0,[59,74,65,86], '*', 19, 7, 6, 2)
m1 = Monkey(1,[62,84,72,91,68,78,51], '+', 1, 2, 2, 0)
m2 = Monkey(2,[78,84,96], '+', 8, 19, 6, 5)
m3 = Monkey(3,[97,86], '**', 2, 3, 1, 0)
m4 = Monkey(4,[50], '+', 6, 13, 3, 1)
m5 = Monkey(5,[73,65,69,65,51], '*', 17, 11, 4, 7)
m6 = Monkey(6,[69,82,97,93,82,84,58,63], '+', 5, 5, 5, 7)
m7 = Monkey(7,[81,78,82,76,79,80], '+', 3, 17, 3, 4)
monkeys = [m0,m1,m2,m3,m4,m5,m6,m7]

for i in range(10000):
    for monkey in monkeys:
        while monkey.items:
            throw_to_monkey, item = monkey.inspect_item()
            monkeys[throw_to_monkey].items.append(item)
max_inspect_count = 0
for monkey in monkeys:
    if monkey.inspect_item_count>max_inspect_count:
        max_inspect_count=monkey.inspect_item_count
next_max_inspect_count = 0
for monkey in monkeys:
    if monkey.inspect_item_count>next_max_inspect_count and monkey.inspect_item_count<max_inspect_count:
        next_max_inspect_count=monkey.inspect_item_count
monkey_business_score = max_inspect_count*next_max_inspect_count
print(monkey_business_score)