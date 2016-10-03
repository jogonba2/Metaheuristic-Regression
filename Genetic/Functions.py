#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Functions.py
#  
#  José Ángel González Barba (TIA - IARFID)
# https://en.wikipedia.org/wiki/List_of_mathematical_functions

from math import sqrt,log,e,sin,cos,exp,acos,asin,atan,tan,tanh,acosh,asinh,atanh,cosh,sinh
from random import shuffle

def div(a,b):   return float(a)/float(b)
def dot(a,b):   return float(a)*float(b)
def mod(a,b):   return int(a)%int(b)
def add(a,b):   return float(a)+float(b)
def sub(a,b):   return float(a)-float(b)
#def left(a,b):  return a
#def right(a,b): return b 

def idt(a):     return float(a)
def zero(a):    return 0.0
def one(a):     return 1.1
def sigmoid(a): return 1.0/(1.0+(exp(-float(a))))
def derivative_sigmoid(a): return sigmoid(float(a))*(1.0-sigmoid(float(a)))
def derivative_tanh(a): 1.0-(tanh(float(a))**2)
def pow_two(a):   return a**2
def pow_three(a): return a**3
def pow_four(a):  return a**4
def pow_five(a):  return a**5
#def neg(a):      return -a
#def abs(a):      return abs(a)
#def sign(a):     return 1 if a>0 else 0 if a==0 else -1

def get_functions(n_features):
    
    O = [div,dot,mod,add,sub]

    F = [exp,sqrt,log,sin,cos,exp,acos,asin,atan,tan,tanh,idt,zero,one,sigmoid,derivative_sigmoid,
	 derivative_tanh,tanh,acosh,asinh,atanh,cosh,sinh,pow_two,pow_three,pow_four,pow_five]

    C = [i for i in xrange(n_features)] ; shuffle(C)
    
    return O, F, C
