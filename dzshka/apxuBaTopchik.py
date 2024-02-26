def apxuBaTop():
    with open("C:\\dzshka\\do.txt", "r", encoding="utf-8") as f:
        txt = f.read()

    z_prepinaniya = {'.', ',', ';', ':', '!', '?'}
    posle = ''
    probel = False

    for znak in txt:
        if probel:
            if znak != ' ':
                posle += znak
                probel = False
        else:
            if znak in z_prepinaniya:
                probel = True
                posle += znak
            elif znak != ' ':
                posle += znak
            else:
                if posle and posle[-1] not in z_prepinaniya:
                    posle += znak

    with open("C:\\dzshka\\posle.txt", "w") as f:
        f.write(posle)

apxuBaTop()