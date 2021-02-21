a = input()
b = a[len(a) // 2]
c = len(a) - 1
if a[0] == b:
    print(a[1:c])
elif not a[0] == b:
    print(b)
