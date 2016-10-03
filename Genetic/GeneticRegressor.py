#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  GeneticRegressor.py
#
#  José Ángel González Barba (TIA - IARFID)

from deap import base, creator, tools, algorithms
from numpy import float64,mean,std,min,max,array
from Fitness import evaluate_regression, evaluate_classification
from Individual import create_individual
from Crossover import crossover_two_points
from Mutation import mutate_replace,mutate_shift

def predict(regressor,Xt):
    ind = regressor[0]
    two_f,one_f,idx,res   = ind[0],ind[1],ind[2],0
    ind = None
    Yt  = []
    for i in xrange(Xt.shape[0]):
	zero_one_f,zero_idx,res = one_f[0],idx[0],0
	try: 
	    res = zero_one_f(Xt[i][zero_idx])
	    for j in xrange(1,len(idx)):
		act_one_f, act_two_f, act_idx = one_f[j], two_f[j-1], idx[j]
		try: res = act_two_f(res,act_one_f(Xt[i][act_idx]))
		except: continue
	    Yt.append(res)
	except: return 999999.0,
    return array(Yt)
    
def evaluate(regressor,Xt,Yt): return evaluate_regression(regressor,Xt,Yt)[0]

def fit(XT,YT,prob_mutate_two_arity,prob_mutate_one_arity,prob_mutate_features,
	population_size,iterations,prob_mating,prob_mutating,tournsize,O,F,C):
	    
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    _create_individual = create_individual(XT.shape[1],O,F,C)
    toolbox.register("individual", tools.initRepeat, creator.Individual,_create_individual,n=1)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", evaluate_regression,XT=XT,YT=YT)
    toolbox.register("mate", crossover_two_points)
    toolbox.register("mutate", mutate_replace,prob_mutate_two_arity=prob_mutate_two_arity,
			       prob_mutate_one_arity=prob_mutate_one_arity,
			       prob_mutate_features=prob_mutate_features,O=O,F=F,C=C)
    toolbox.register("select", tools.selTournament, tournsize=tournsize)
    population = toolbox.population(n=population_size)
    
    hof = tools.ParetoFront()
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg",mean,axis=0)
    stats.register("std",std,axis=0)
    stats.register("min",min,axis=0)
    stats.register("max",max,axis=0)
    
    population, logbook = algorithms.eaSimple(population, toolbox,cxpb=prob_mating, mutpb=prob_mutating, 
					      ngen=iterations, stats=stats, halloffame=hof)
    return population, logbook, hof

def __fenotype__(regressor):
    reg = regressor[0]
    two_f,one_f,idx,res  = reg[0],reg[1],reg[2],""
    res += one_f[0].__name__+"(X["+str(idx[0])+"])"
    for i in xrange(1,len(idx)): res = two_f[i-1].__name__+"("+res+","+one_f[i].__name__+"(X["+str(idx[i])+"]))"
    return res
