sp = {}
# comment

def function_add(b, *aa): # b - class, aa list of parent
    l = list(aa)
    if b not in sp:
        sp[b] = []
        print(l)
        if len(l)>1:
            for q in l:
                sp[b].append(l[q])
    else:
        if len(l) > 1:
            for q in l:
                sp[b].append(l[q])
def function_get(a, b):
    if a == b:
        print('Yes')
        #return True
    else:
        if b in sp and a in sp[b]:
            print('Yes')
            return True
        else:
            print('No')
            return True


n = int(input())
for i in range(n):
    stroka = input().split()
    if len(stroka) > 1:
        function_add(stroka[0], stroka[2::])
    else:
        function_add(stroka[0])
print(sp)
q = int(input())
for j in range(q):
    s = str.split(input())
    function_get(s[0], s[1])
