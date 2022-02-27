a = True
while a:
    ps = input("Напиши свой красивый пороль")
    if len(ps) < 8:
        print("Короткий")
    else:
        print("ОК")
        a = False
        print("Отличный пороль!!!!")