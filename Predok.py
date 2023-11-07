class Klass:
    def __init__(self):
        self.name = ''
        self.parent = []


sp = []
n = int(input())
for i in range(n):
    stroka = input().split()
    x = Klass()
    x.name = stroka[0]
    if len(stroka) > 1:
        stroka.pop(0)
        stroka.pop(0)
        x.parent = stroka
    sp.append(x)


q = int(input())
for j in range(q):
    s = str.split(input())
    for k in range(len(sp)):
        if s[0] == sp[k].name and s[1] in sp[k].parent:
            print('Yes')
            break
        else:
            print('No')

