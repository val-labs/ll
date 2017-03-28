#!/usr/bin/env python
def push(x,y): x.append(y) ; return x
def pop(x): return x.pop()
import sys
fni=sys.argv[1] ; fno=fni[:-1]+'o'
fi,fo=open(fni),open(fno,'w')
stack = [ 0 ]
prev_line = ''
N=-1
def count_spaces(line):
    for n,c in enumerate(line):
        if c!=' ':
            return n
    return -1
def do_line(last_line=False):
    global c
    c = curr = count_spaces(curr_line)
    p = prev = count_spaces(prev_line)
    if c == -1: c = 0
    if p == -1: p = 0
    if last_line: c = 0
    if prev == -1:
        print(".")
    else:
        line_str = prev_line
        if c > p:
            ch = '>'
            line_str = '('+line_str
            push(stack, c)
        elif c == p:
            ch = '='
            line_str = '.'+line_str+close(c)
        elif c < p:
            ch = '<'
            line_str = ':'+line_str+close(c)
            pass
        print("x", N, ch, c, curr, p, prev,
              last_line, line_str)
        
def close(c):
    ret = []
    while stack[-1] > c:
        pop(stack)
        push(ret, ')')
        pass
    return ''.join(ret)
for N,line in enumerate(fi):
    curr_line = line[:-1]
    if N>0:
        do_line()
    prev_line = curr_line
    pass
do_line(last_line=True)
