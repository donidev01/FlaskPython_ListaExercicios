def lst02ex10():
    msg = "n"
    if msg != None:
        msg = msg.upper()
        if msg.startswith("M"):
            return "M-matutino"

        if msg.startswith("V"):
            return "V-Vespertino"

        if msg.startswith("N"):
            return "N- Noturno"


print(lst02ex10())
