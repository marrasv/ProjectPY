class Buffer:
    def __init__(self):
        self.ls = []

    def add(self, *a):
        for j in range(len(a)):
            self.ls.append(a[j])
        while len(self.ls) > 4:
            summ = 0
            for i in range(5):
                summ += self.ls[0]
                self.ls.pop(0)
            print(summ)

    def get_current_part(self):
        return self.ls


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()
