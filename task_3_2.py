n = int(input("количество гостей:"))
if n > 50:
    print("ресторан")
elif 20 <= n <= 50:
    print("кафе")
elif n < 20:
    print("дом")
