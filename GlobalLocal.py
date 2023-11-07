sp = {
    'global': {
        'parent': None,
        'vars': []
    }
}


def function_add(ns, v):
    sp[ns]['vars'].append(v)


def function_create(ns, par):
    sp[ns] = {}
    sp[ns]['parent'] = par
    sp[ns]['vars'] = []


def function_get(ns, v):
    if v in sp[ns]['vars']:
        print(ns)
    elif sp[ns]['parent'] is None:
        print('None')
    else:
        function_get(sp[ns]['parent'], v)


n = int(input())
for i in range(n):
    kom, nam, arg = input().split()
    if kom == 'add':
        function_add(nam, arg)
    elif kom == 'create':
        function_create(nam, arg)
    elif kom == 'get':
        function_get(nam, arg)
    else:
        break
    