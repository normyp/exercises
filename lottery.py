import random

class Lottery():
    def __init__(self, lottery_list=[]):
        self.lottery_list = lottery_list

    def select_lottery(self):
        r = random.randint(0, 7)
        return self.lottery_list[r]

lot1 = Lottery(["a", "b", "c", "d", 1, 2, 3, 4])
lottery_output = []
for i in range(0, 4):
    lottery_output.append(lot1.select_lottery())
print(lottery_output)

my_ticket = ["b", 2, 3, "d"]
won = False
count = 0
while(won == False):
    count += 1
    lottery_output = []
    for i in range(0, 4):
        lottery_output.append(lot1.select_lottery())
    print(lottery_output)
    print("Lottery has rolled", count, "times")
    if (lottery_output == my_ticket):
        won = True
