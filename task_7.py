a = int(input())


def sm(q):
    print("дюймы в сантиметры")
    return q * 2.54


def dm(q):
    print("сантиметры в дюймы")
    return q / 2.54


def km(q):
    print("мили в километры")
    return q * 1.609


def ml(q):
    print("километры в мили")
    return q / 1.609


def kg(q):
    print("фунты в килограммы")
    return q * 0.45


def ft(q):
    print("килограммы в фунты")
    return q / 0.45


def gr(q):
    print("унции в гаммы")
    return q * 28.3


def oz(q):
    print("граммы в унции")
    return q / 28.3


def ltr1(q):
    print("галлон в литры")
    return q * 4.55


def gal(q):
    print("литры в галлоны")
    return q / 4.55


def ltr2(q):
    print("пинты в литры")
    return q * 0.568


def pint(q):
    print("литры в пинты")
    return q / 0.568


dc = {
    1: sm,
    2: dm,
    3: km,
    4: ml,
    5: kg,
    6: ft,
    7: gr,
    8: oz,
    9: ltr1,
    10: gal,
    11: ltr2,
    12: pint
}
while a != 0:
    if 1 <= a <= 12:
        x = int(input())
        print(dc[a](x))
    else:
        print("номер функции не от 1 до 12")
    print("ведите номер функции")
    a = int(input())
