import random


class Dice:
    def roll(self):
        self.tup = (random.randint(1,6), random.randint(1,6))

    def print_result(self):
        print(f'({self.tup[0]}, {self.tup[1]})')


turn = Dice()
turn.roll()
turn.print_result()
    

# print(f'({random.randint(1,6)}, {random.randint(1,6)})')  # values b/w a preset range ints