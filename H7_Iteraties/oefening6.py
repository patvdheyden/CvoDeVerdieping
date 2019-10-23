from pcinput import getLetter

doorgaan = True
while doorgaan:
    print("Goed bezig")
    stop = getLetter("Stoppen? J/N")
    if stop == "J":
        doorgaan = False
print("Gestopt")
