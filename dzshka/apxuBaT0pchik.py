def apxuBaTop():
    with open("do.txt", "r") as f:
        txt = f.read()

    z_prepinaniya = {'.', ',', '!', '?'}
    words = txt.split()

    posle = []
    for word in words:
        if word[-1] in z_prepinaniya:
            posle.append(word)
        else:
            posle.append(word + ' ')

    posle_txt = ''.join(posle)

    with open("posle.txt", "w") as f:
        f.write(posle_txt)

apxuBaTop()