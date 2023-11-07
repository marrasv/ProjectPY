sp = {}


def function_add(ch, par):
    if ch not in sp:
        sp[ch] = set()
    for i in range(len(par)):
        sp[ch].add(par[i])


def function_get(par, ch):
    if ch in sp:
        if par in sp[ch]:
            print('Yes')
        else:
            for k in range(len(sp[ch])):
                function_get(sp[ch][k], ch)
    else:
        print('No')

n = int(input())
for i in range(n):
    stroka = input().split()
    l = stroka[2::]
    function_add(stroka[0], l)
print(sp)
m = int(input())
for j in range(m):
    stroka = input().split()
    function_get(stroka[0], stroka[1])