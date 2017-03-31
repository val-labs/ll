#!/usr/bin/env python


import sys
import string


def join(a,s=None):
    if s is None: s = ''
    return string.join(a,s)


def push(x,y): x.append(y); return x
def pop(x): return x.pop()


class Parser:
    def __init__(_):
        _.row, _.col = -1, -1
        _.state = 0
        _.expr  = ['P']
        _.prev  = []
        pass

    def opn_expr(_, val=None):
        push(_.prev, _.expr)
        _.expr = val or []
        pass

    def cls_expr(_, val):
        _.expr = pop(_.prev)
        push(_.expr, val)
        pass

    def s0(_, ch):
        if ch in ' \t\r\n':
            pass
        elif ch in '([{':
            _.opn_expr([':'])
        elif ch in ')]}':
            _.cls_expr(_.expr)
        elif ch in '\"':
            _.opn_expr(['$'])
            _.state = 2
        else:
            _.opn_expr(['^',ch])
            _.state = 1
            pass
        pass

    def s1(_, ch):
        if ch in ' \t\r\n':
            _.cls_expr(join(_.expr))
            _.state = 0
        elif ch in '\\':
            push(_.expr, ch)
            _.state = 4
        elif ch in '([{':
            _.opn_expr()
            _.state = 0
        elif ch in ')]}':
            _.cls_expr(join(_.expr))
            _.cls_expr(_.expr)
            _.state = 0
        else:
            push(_.expr, ch)
            pass
        pass

    def s2(_, ch):
        if ch in '\"':
            _.cls_expr(join(_.expr))
            _.state = 0
        elif ch in '\\':
            push(_.expr, ch)
            _.state = 3
        else:
            push(_.expr, ch)
            pass
        pass
        
    def s3(_, ch):
        push(_.expr, ch)
        _.state = 2
        pass
        
    def s4(_, ch):
        push(_.expr, ch)
        _.state = 1
        pass
        
    def prs(_, ch):
        print "=======>", _.state, _.expr, _.prev
        return getattr(_, 's%d'%_.state)(ch)

    def parse_file(_, f):
        for _.row, line in enumerate(sys.stdin):
            print("LINE", repr(line))
            for _.col, ch in enumerate(line):
                print("  ch", repr(ch))
                _.prs(ch)
        print "X======>", _.state, _.expr, _.prev
        if _.state or _.prev:
            raise "ERR"
        return _.expr


Parser().parse_file(sys.stdin)
