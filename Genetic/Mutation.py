#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Mutation.py
#
#  José Ángel González Barba (TIA - IARFID)

from deap import creator
from random import random,choice,randint

def mutate_shift(individual,prob_mutate_two_arity,prob_mutate_one_arity,prob_mutate_features):
	       
    individual = individual[0]
    # Mutate two-arity functions (ops) #
    for i in xrange(len(individual[0])):
	if random()<prob_mutate_two_arity:
	    pos_one,pos_two = randint(0,len(individual[0])-1),randint(0,len(individual[0])-1)
	    individual[0][pos_one],individual[0][pos_two] = individual[0][pos_two],individual[0][pos_one]
	    #print "A"

    # Mutate one-arity functions #
    for i in xrange(len(individual[1])):
	if random()<prob_mutate_one_arity:
	    pos_one,pos_two = randint(0,len(individual[1])-1),randint(0,len(individual[1])-1)
	    individual[1][pos_one],individual[1][pos_two] = individual[1][pos_two],individual[1][pos_one]
	    #print "B"
	    
    # Mutate features            #
    for i in xrange(len(individual[2])):
	if random()<prob_mutate_features:
	    pos_one,pos_two = randint(0,len(individual[2])-1),randint(0,len(individual[2])-1)
	    individual[2][pos_one],individual[2][pos_two] = individual[2][pos_two],individual[2][pos_one]
	    
    return creator.Individual([individual]), 

def mutate_replace(individual,prob_mutate_two_arity,prob_mutate_one_arity,
		   prob_mutate_features,O,F,C):
    individual = individual[0]
    # Mutate two-arity functions (ops) #
    for i in xrange(len(individual[0])):
	if random()<prob_mutate_two_arity: individual[0][i] = choice(O)
	    
    # Mutate one-arity functions #
    for i in xrange(len(individual[1])):
	if random()<prob_mutate_one_arity: individual[1][i] = choice(F)
	
    # Mutate features            #
    for i in xrange(len(individual[2])):
	if random()<prob_mutate_features: individual[2][i] = choice(C)
    
    return creator.Individual([individual]),
