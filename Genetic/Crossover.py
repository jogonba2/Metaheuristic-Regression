#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Crossover.py
#
#  José Ángel González Barba (TIA - IARFID)

from random import randint
from deap import creator

# Revisar, posible bug con los indices en la creacion de nuevos individuos (new_ind_one,new_ind_two) #
def crossover_two_points(ind_one,ind_two):
    new_ind_one,new_ind_two = [],[]
    ind_one,ind_two = ind_one[0],ind_two[0]
    for i in xrange(0,3):
	p_min = randint(0,len(ind_one[0])-3)
	p_max = randint(p_min+1,len(ind_one[0])-2)
	new_ind_one.append(ind_one[i][0:p_min]+ind_two[i][p_min:p_max]+ind_one[i][p_max:])
	new_ind_two.append(ind_two[i][0:p_min]+ind_one[i][p_min:p_max]+ind_two[i][p_max:])
    return creator.Individual([new_ind_one]), creator.Individual([new_ind_two])
