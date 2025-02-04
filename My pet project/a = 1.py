b = "шишка"
for i in range(6000, 6666+1):
    c = i % 10
    d = i % 100
    if i < 10:
        if i == 1:
            b = "шишка"
        elif i < 5 and i > 1:
            b ="шишки"
        else:
            b = "шишек"

    elif (i >= 10 and i <= 20) or (d >= 10 and d<=20):
        b = "шишек"
        
    elif i > 20:
        if c == 0:
            b = "шишек"
        elif c == 1:
            b = "шишка"
        elif c > 1 and c < 5:
            b = "шишки"
        else:
            b = "шишек"
    print(f'{i} {b}')
    

