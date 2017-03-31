

import sys


G = {}


def prn(e,*args):
    print " ====> PRN", repr(args)
    return [list(args)]


G['set'] = lambda e,k,v: [e.xSET(k,v)]
G['prn'] = prn
G['stdin' ] = sys.stdin
G['stdout'] = sys.stdout
G['stderr'] = sys.stderr
G['readline'] = lambda e,f: f.readline()
G['x'] = 109
G['y'] = 208
