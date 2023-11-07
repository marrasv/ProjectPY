class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.n = 0

    def can_add(self, v):
        if v <= (self.capacity - self.n):
            return True
        else:
            return False

    def add(self, v):
        self.n += v


x = MoneyBox(15)
x.add(5)
x.add(11)
print(x.can_add(11))
