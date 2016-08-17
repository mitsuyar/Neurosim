# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:23:15 2016

@author: Ryoha
"""
from netpyne import specs,sim
netParams = specs.NetParams()
simConfig = specs.SimConfig()
#popParams
netParams.addPopParams('S', {'cellType': 'S', 'numCells':1, 'cellModel': 'HH'})
netParams.addPopParams('M',{'cellType': 'M', 'numCells':1, 'cellModel':'HH'})

#cellRules
cellRule = {'conds': {'popLabel': 'S', 'popLabel':'M'}, 'secs':{}}
cellRule['secs']['soma'] = {'geom':{}, 'mechs':{}}
cellRule['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}
cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}
cellRule['secs']['dend'] = {'geom' : {}, 'topol':{}, 'mechs':{}}
cellRule['secs']['dend']['geom']= {'diam': 5.0, 'L': 150.0, 'Ra': 150.0, 'cm': 1}
cellRule['secs']['dend']['mechs']['pas'] = {'g': 0.0000357, 'e': -70}
cellRule['secs']['dend']['topol'] = {'parentSec': 'soma', 'parentX':1.0, 'childX': 0}
netParams.addCellParams('rule', cellRule)

#synMechs
netParams.addSynMechParams('exc', {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 5.0, 'e': 0})

#connRules
netParams.addConnParams('S->M',{'preConds': {'popLabel': 'S'},'postConds': {'popLabel': 'M'}, 'delay': 5, 'synsPerConn': 3, 'sec':'dend', 'loc': [0.3,0.6,0.9],'synMech':'exc'})
#stims
netParams.addStimSourceParams('Input_1',{'type': 'VClamp', 'dur':[0,10,50],'amp':[20,40,50],'gain':1, 'rstim':5, 'tau1':5, 'tau2':3, 'i':5})
netParams.addStimTargetParams('Input_1 -> S', {'source':'Input_1', 'sec':'soma', 'loc': 0,'delay': 0, 'conds':{'popLabel': 'S'}})
#netParams.addStimTargetParams('Input_2 -> S', {'source':'Input_1', 'sec':'soma', 'loc': 0,'delay': 0, 'conds':{'popLabel': 'S'}})
#netParams.addStimTargetParams('Input_3 -> S', {'source':'Input_1', 'sec':'soma', 'loc': 0,'delay': 0, 'conds':{'popLabel': 'S'}})
#netParams.addStimTargetParams('Input_4 -> S', {'source':'Input_1', 'sec':'soma', 'loc': 0,'delay': 0, 'conds':{'popLabel': 'S'}})
#netParams.addStimTargetParams('Input_5 -> S', {'source':'Input_1', 'sec':'soma', 'loc': 0,'delay': 0,'conds':{'popLabel': 'S'}})
#simConfig
simConfig = specs.SimConfig() 
simConfig.duration = 100
simConfig.dt = 0.025
simConfig.verbose = False
simConfig.recordTraces = {'V_Soma': {'sec':'soma', 'loc':0.5, 'var':'v', 'popLabel':'S'}}
simConfig.recordStep = 0.1
simConfig.filename = 'model_output'
simConfig.savePickle = False

simConfig.addAnalysis('plotRaster', True)
simConfig.addAnalysis('plotTraces', {'include': [1]})
simConfig.addAnalysis('plot2Dnet', True)

sim.createSimulateAnalyze(netParams, simConfig)