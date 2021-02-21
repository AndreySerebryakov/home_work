a = str(input())
if len(a) > 10:
    b = a + "!!!"
    print(b)
elif len(a) < 10:
    print(a[1])
elif len(a) == 10:
    print("длина строки равна 10 символам")
