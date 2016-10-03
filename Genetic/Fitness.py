#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Fitness.py
#
#  José Ángel González Barba (TIA - IARFID)

from numpy import float64

def evaluate_regression(individual,XT,YT):
    ind = individual[0]
    two_f,one_f,idx,res,mse   = ind[0],ind[1],ind[2],0,0
    ind = None
    for i in xrange(XT.shape[0]):
	zero_one_f,zero_idx,res = one_f[0],idx[0],0
	try: 
	    res = zero_one_f(XT[i][zero_idx])
	    for j in xrange(1,len(idx)):
		act_one_f, act_two_f, act_idx = one_f[j], two_f[j-1], idx[j]
		try: res = act_two_f(res,act_one_f(XT[i][act_idx]))
		except: continue
	    mse += (res-YT[i])**2
	    if mse==float64("inf"): return 999999.0,
	except: return 999999.0,
    return (1.0/XT.shape[0])*mse,
    
def evaluate_classification(individual,XT,YT): pass
