from termcolor import colored

UL, UR = '╔', '╗'
SL, SR = '╠', '║'
DL, DR = '╚', '╝'
AL, AR = '═', '>'


def padded(
    line, info=None, width=100, intro='>', outro='<', filler='.', chopped='..'
):
    # cleanup input
    line = ''.join([' ', line.strip()]) if line else ''
    info = info.strip() if info else ''

    # determine available width
    width -= sum([len(intro), len(outro), len(line), len(info)])
    if width < 0:
        # chop off overflowing text
        line = line[:len(line)+width]
        if chopped:
            # place chopped characters (if set)
            chopped = chopped.strip()
            line = ' '.join([line[:len(line)-(len(chopped)+1)], chopped])

    return ''.join(e for e in [
        intro,
        info,
        line,
        ''.join(filler for _ in range(width)),
        outro
    ] if e)


def box(rnum, nbeds, *extras):
    arrow = (AL+AR)
    res = [
        # head line
        padded(
           'Hfst. {:03d} <'.format(rnum), (AL+AL+arrow),
            intro=UL, outro=UR, filler=AL
        ),
        # first line
        padded(
            'Oef. {:03d}'.format(nbeds), arrow,
            intro=SL, outro=SR, filler=' '
        ),
    ]
    # following lines
    res.extend(padded(e, arrow, intro=SL, outro=SR, filler=' ') for e in extras)
    # bottom line
    res.append(padded(None, None, intro=DL, outro=DR, filler=AL))

    return '\n'.join(res)