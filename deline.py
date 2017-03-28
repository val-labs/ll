#!/usr/bin/env python

import sys
import string


def join(a,s=None):
    if s is None: s = ''
    return string.join(a,s)
Stack = [ 0 ]


def push(x,y): x.append(y); return x
def pop(x): return x.pop()


def chomp(s):
    if s and s[-1]=='\n':
        return s[:-1]
    return s


def count_spaces(s):
    for n,c in enumerate(s):
        if c != ' ':
            return n
    return 0


def do_line(prev_line, curr_line):

    def go_in():
        Stack.append(c)
        print join(['[', prev_line ])

    def go_out():
        y = []
        while c < Stack[-1]:
            y.append(']')
            Stack.pop()
            pass
        print join([' ', prev_line, join(y)])

    if prev_line is None:
        return
    p = count_spaces(prev_line)
    c = count_spaces(curr_line)
    prev_line = '{'+prev_line+'}'
    if c > p: go_in()
    else:     go_out()


def do_file(f):
    prev_line = None
    for line in f:
        curr_line = chomp(line)
        do_line(prev_line, curr_line)
        prev_line = curr_line
        pass
    do_line(prev_line, '')


do_file(sys.stdin)
