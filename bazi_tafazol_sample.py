def game(number):
    number1 = str(number)
    list = []
    for ch in number1 :
        list.append(int(ch))
        tafazol = max(list)-min(list)
    return tafazol
pass
