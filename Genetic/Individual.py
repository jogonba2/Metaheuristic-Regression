#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Individual.py
#
#  José Ángel González Barba (TIA - IARFID)

from random import choice

def create_individual(n_features,O,F,C): 
    # Clausura para ejecutar con deap #
    def _create_individual():
	return [[choice(O) for i in xrange(n_features-1)],
		 [choice(F) for i in xrange(n_features)],
		 C]
    return _create_individual
