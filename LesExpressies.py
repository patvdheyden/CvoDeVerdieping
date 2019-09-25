print((((2 * 3) / 4 + (5 - 6 / 7) * 8)))

# String functions

def left(s, amount):
    return s[:amount]


def right(s, amount):
    return s[-amount:]


def mid(s, offset, amount):
    return s[offset:offset + amount]


BeginTijd = "14:00"
BeginUur = left(BeginTijd, 2)
BeginMinuten = right(BeginTijd,2)

AlarmTijdTotaal = 535
AlarmInDagen = 535 // 24  # Gehele deling
AlarmInUren = 535 % 24  # Rest van de deling (mod) zijn de uren
print(AlarmInDagen)
print(AlarmInUren)
print("Het alarm is binnen", str(AlarmInDagen), "Dagen en", str(AlarmInUren), "dus om", str(BeginUur).rjust(2,"0")+":"+str(AlarmInUren).rjust(2,"0"))


