def isDigit(x):
    try:
        x = int(x)
        return isinstance(x, int)
    except ValueError:
        return False


file = '2020ICPCNanjing'
f = open(file, 'r')
ranklist = f.read().split('\n')
s = ""
for i in ranklist:
    if (isDigit(i[0])):
        print(s)
        s = i
    else:
        s = s + i
print(s)
