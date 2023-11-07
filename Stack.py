class ExtendedStack(list):
    def sum(self):
        val = self[len(self)-1] + self[len(self)-2]
        self.pop()
        self.pop()
        self.append(val)
        return val

    def sub(self):
        val = self[len(self)-1] - self[len(self) - 2]
        self.pop()
        self.pop()
        self.append(val)

    def mul(self):
        val = self[len(self)-1] * self[len(self) - 2]
        self.pop()
        self.pop()
        self.append(val)

    def div(self):
        val = self[len(self)-1] // self[len(self) - 2]
        self.pop()
        self.pop()
        self.append(val)


b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = ExtendedStack(b)
print(x, x.sum())
