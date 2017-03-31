

G = {}


def prn(*args):
    print "PRN", repr(args)
    return [args[0],22,33]


G['prn'] = prn
G['x'] = 109
G['y'] = 208
