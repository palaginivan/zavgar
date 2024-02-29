def pa3apxuBaTopchik():
    with open("posle.txt", "r") as f:
        txt = f.read()

    z_prepinaniya = {'.', ',', '!', '?'}

    for znak in z_prepinaniya:
        txt = txt.replace(znak, znak + ' ')

    with open("esheposle.txt", "w") as f:
        f.write(txt)

pa3apxuBaTopchik()


















