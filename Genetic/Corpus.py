#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Corpus.py
#
#  José Ángel González Barba (TIA - IARFID)

def prepare_corpus(corpus,perc_train,shuffle=False):
    boston      = corpus()
    data,target = boston["data"],boston["target"]
    XT,YT = data[0:int(perc_train*data.shape[0])],target[0:int(perc_train*target.shape[0])]
    Xt,Yt = data[int(perc_train*data.shape[0])+1:],target[int(perc_train*target.shape[0])+1:]
    n_features  = XT.shape[1]
    return XT, YT, Xt, Yt, n_features
