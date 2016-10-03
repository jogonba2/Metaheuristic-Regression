#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  GeneticClassifier.py
#
#  José Ángel González Barba (TIA - IARFID)

from deap import base, creator, tools, algorithms
from numpy import float64,mean,std,min,max
from Fitness import evaluate_regression, evaluate_classification
from Individual import create_individual
from Crossover import crossover_two_points
from Mutation import mutate_replace,mutate_shift
from multiprocessing import pool

def fit(XT,YT,prob_mutate_two_arity,prob_mutate_one_arity,prob_mutate_features,
	population_size,iterations,prob_mating,prob_mutating,tournsize,O,F,C):
	    
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    _create_individual = create_individual(n_features,O,F,C)
    toolbox.register("individual", tools.initRepeat, creator.Individual,_create_individual,n=1)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", Fitness.evaluate_regression,XT=XT,YT=YT)
    toolbox.register("mate", crossover_two_points)
    toolbox.register("mutate", mutate_shift,prob_mutate_two_arity=prob_mutate_two_arity,
			       prob_mutate_one_arity=prob_mutate_one_arity,
			       prob_mutate_features=prob_mutate_features)#,O=O,F=F,C=C)
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
