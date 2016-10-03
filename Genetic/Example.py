#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Example.py
#
#  José Ángel González Barba (TIA - IARFID)

from sklearn.datasets import load_boston
from sklearn.preprocessing import normalize
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from random import random, shuffle, choice, randint
from warnings import filterwarnings
from Corpus import prepare_corpus
from Functions import *
from deap import creator
import pickle
import GeneticRegressor
import GeneticClassifier

filterwarnings("ignore")

if __name__ == "__main__":
    XT, YT, Xt, Yt, n_features = prepare_corpus(load_boston,0.8,shuffle=False)
    O, F, C        = get_functions(n_features)
    population, logbook, hof = GeneticRegressor.fit(XT=XT,YT=YT,prob_mutate_two_arity=0.4,prob_mutate_one_arity=0.4,prob_mutate_features=0.4,
						    population_size=20,iterations=75,prob_mating=0.8,prob_mutating=0.3,tournsize=5,O=O,F=F,C=C)
    regressor = hof[0]
    
    # Predicting #
    aYt = GeneticRegressor.predict(regressor,Xt)
    
    # Evaluating model #
    print GeneticRegressor.evaluate(regressor,Xt,Yt)
    
    # Persistence #
    with open("regressor.bin","wb") as fd: pickle.dump(regressor,fd)
    with open("regressor.bin","rb") as fd: regressor = pickle.load(fd)
    
    # Printing fenotype #
    print GeneticRegressor.__fenotype__(regressor)
    
    # Results with SVM(Linear,RBF,Poly) -> Linear 19000 mse (muy lento), RBF 91, rápido, poly (muy lento) (Genetico mejor que los tres) #
    #svr_lin = SVR(kernel='poly', C=1e3, degree=2)
    #y_rbf = svr_lin.fit(XT, YT).predict(Xt)
    #print mean_squared_error(y_rbf,Yt)
    
    # Resuls with DecissionTree(depth=2(41),3(42.96),4(65.50),5(55.58))
    #regr_tree = DecisionTreeRegressor(max_depth=5)
    #regr_tree.fit(XT,YT)
    #print mean_squared_error(regr_tree.predict(Xt),Yt)

    # Mejores resultados obtenidos con el regresor genético #
    """
    · 24.860844012 test mse, 73.009 train mse (statistics in best_model_1.txt):
      add(sub(add(div(sub(div(add(add(mod(sub(mod(add(acos(X[3]),asinh(X[10])),pow_five(X[4])),
      acos(X[5])),sigmoid(X[11])),derivative_sigmoid(X[3])),exp(X[3])),sinh(X[4])),atanh(X[10])),
      atan(X[3])),sqrt(X[1])),acos(X[2])),sqrt(X[11]))
    """
    #for i in xrange(len(Yt)):
	#print Yt[i] , " -> " , aYt[i] 
