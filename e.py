#!/usr/bin/env python

import os, sys, time
from g import G


class Env:
    ARGS=[]
    def __init__(_,B,C): _.B, _.C, _.D, _.E = B, C, [], {}
    def e(_,_e): _.E = _e ; return _
    def xLOOKUP(_,n):
        x = _
        ret = x.E.get(n)
        while not ret:
            x = x.B
            ret = x.E.get(n)
        return ret
    def xSET(_,n,v):
        x = _
        ret = x.E.get(n)
        while not ret:
            if not x.B:
                x = _.B
                break
            x = x.B
            ret = x.E.get(n)
            pass
        x.E[n] = v
        return _
    def step(_):
        #print "STEP", time.time(), repr((_.B, _.C, _.D, _.E))
        try:
            x = _.C.pop(0)
            _.D.append(int(x))
        except IndexError: # empty
            if _.B:
                _.B.D.extend(_.D)
            return _.B
        except TypeError: # a list
            return Env(_, x)
        except ValueError: # a string
            if x == "**":
                Env.ARGS = _.D.pop(0)(_, *_.D)
                _.D = [Env.ARGS[0]]
            elif x == ";;":
                _.D = []
            elif x[0] == '^':
                _.D.append(_.xLOOKUP(x[1:]))
            elif x[0] == '$':
                _.D.append(x[1:])
            elif x[0] == '#':
                print "SET TO", x
            else:
                raise Exception()
        return _
    def run(_):
        ovm = vm = _
        while vm:
            ovm = vm
            vm = vm.step()
            pass
        print "return", ovm.D
        return ovm.D
    pass


def VM(C):
    return Env(None, C).e(G)


print '='*80
VM(["^prn","100","**"]).run()
print '='*80
VM([["^prn","101","**"],
    ["^prn","102","**"]]).run()
print '='*80
VM([["^prn","^x","**"], ";;",
    ["^prn","$yy","**"],";;",
    ["^prn","^y","**"]]).run()
print '='*80
VM([["#1:4","^set","$x","$qaz","**"], ";;",
    ["^set","$v","$qaz2","**"], ";;",
    ["^prn","^v","**"]]).run()
print '='*80
