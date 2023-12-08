running = True

# En dictionary på alla bokstäver och vad dom blir
bokstavera = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w",
              "k": "x", "l": "y", "m": "z", "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g",
              "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m"}

siffror = {"1": "5", "2": "6", "3": "7", "4": "8", "5": "9", "6": "0", "7": "1", "8": "2", "9": "3", "0": "4"}


def chiffer(_input):
    _input = list(_input)
    ny_chiffer = ""

    for bokstav in _input:
        if bokstav in bokstavera:
            ny_chiffer += bokstavera[bokstav]
        elif bokstav in siffror:
            ny_chiffer += siffror[bokstav]
        else:
            ny_chiffer += bokstav

    print(ny_chiffer)


def de_chiffer(_input):
    _input = list(_input)
    ny_chiffer = ""

    for bokstav in _input:
        if bokstav in bokstavera.values():
            for key, value in bokstavera.items():
                if value == bokstav:
                    ny_chiffer += key
        else:
            ny_chiffer += bokstav

    print(ny_chiffer)


def start():
    _input = str(input("Vad vill du kryptera eller av kryptera? "))

    if _input == "kryptera":
        _input = str(input("Vad vill du kryptera? "))
        chiffer(_input)
    elif _input == "av kryptera":
        _input = str(input("Vad vill du av kryptera? "))

        de_chiffer(_input)


while running:
    start()
