#!/usr/bin/env python

import os, sys, time
from g import G


class Env:
    ARGS=[]
    def __init__(_,B,C):
        _.B, _.C, _.D, _.E = B, C, [], {}
        pass
    def LOOKUP(_,n):
        #print "LOOKUP", n
        try:
            return _.E[n]
        except KeyError:
            if not _.B:
                raise
            return _.B.LOOKUP(n)
    def step(_):
        print "STEP", time.time(), repr((_.B, _.C, _.D, _.E))
        try:
            x = _.C.pop(0)
            _.D.append(int(x))
        except IndexError: # empty
            if _.B:
                _.B.D.extend(_.D)
            return _.B
        except TypeError: # a list
            #print "TYP", type(x)
            return Env(_, x)
        except ValueError: # a string
            if x == "**":
                Env.ARGS = _.D.pop(0)(*_.D)
                #print "ARGS1 =", Env.ARGS
                _.D = [Env.ARGS[0]]
            elif x == ";;":
                _.D = []
            elif x[0] == '^':
                _.D.append(_.LOOKUP(x[1:]))
            elif x[0] == '$':
                _.D.append(x[1:])
            else:
                raise Exception()
        return _
    def e(_,_e):
        _.E = _e
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
