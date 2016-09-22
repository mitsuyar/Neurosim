# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 10:45:37 2016

@author: Ryoha
"""

from netpyne import specs,sim
netParams = specs.NetParams()

#popParams defined 
"""netParams.addPopParams('S', {'cellType': 'S', 'numCells':2, 'cellModel': 'HH'})
netParams.addPopParams('M',{'cellType': 'M', 'numCells':1, 'cellModel':'HH'})"""
netParams.popParams['Traub_pop'] = {'cellType': 'PYR', 'numCells': 2, 'cellModel': 'Traub'}
 
 
 
 #cellRules for pop
cellRule = netParams.importCellParams(label='PYR_Traub_rule', conds= {'cellType': 'PYR', 'cellModel': 'Traub'}, 
 	fileName='pyr3_traub.hoc', cellName='pyr3')
somaSec = cellRule['secLists']['Soma'][0] 
cellRule['secs'][somaSec]['spikeGenLoc'] = 0.5
 
"""cellRule = {'conds': {'popLabel': 'Traub_pop'}, 'secs':{}}
cellRule['secs']['soma'] = {'geom':{}, 'mechs':{}}
cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.13, 'gkbar': 0.0321, 'gl': 0.002, 'el':-65}
cellRule['secs']['dend'] = {'geom' : {}, 'topol':{}, 'mechs':{}}
cellRule['secs']['dend']['geom']= {'diam': 10, 'L': 15, 'Ra': 120.0, 'cm': 1}
cellRule['secs']['dend']['mechs']['pas'] = {'g': 0.0000321, 'e': -70 }
cellRule['secs']['dend']['topol'] = {'parentSec': 'soma', 'parentX':1.0, 'childX': 0}
netParams.addCellParams('Srule', cellRule)"""
"""cellRule = {'conds':{'popLabel': 'M'}, 'secs':{}}
cellRule['secs']['soma'] = {'geom':{}, 'mechs':{}}
cellRule['secs']['dend'] = {'geom' : {}, 'topol':{}, 'mechs':{}}
cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.13, 'gkbar': 0.0321, 'gl': 0.002, 'el':-65}
cellRule['secs']['dend']['geom']= {'diam': 10, 'L': 15, 'Ra': 120.0, 'cm': 1}
cellRule['secs']['dend']['mechs']['pas'] = {'g': 0.0000321, 'e': -70 }
cellRule['secs']['dend']['topol'] = {'parentSec': 'soma', 'parentX':1.0, 'childX': 0}
netParams.addCellParams('Mrule', cellRule)"""
#SynMech
netParams.addSynMechParams('exc', {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 5.0, 'e': 0})

netParams.addConnParams('S->M',{'preConds': {'popLabel': 'Traub_pop'},'postConds': {'popLabel': 'Traub_pop'}, 'delay': 5,'sec':'dend','loc':1.0,'synMech':'exc'}) 

netParams.addStimSourceParams('Input_1',{'type': 'IClamp', 'delay': 3, 'dur': 10, 'amp':30})
netParams.addStimSourceParams('Input_2',{'type': 'IClamp', 'delay': 5.5, 'dur': 10, 'amp':30})
netParams.addStimSourceParams('Input_3',{'type': 'IClamp', 'delay': 7, 'dur': 10, 'amp':30})
netParams.addStimTargetParams('Input_1 -> S', {'source':'Input_1', 'sec':'dend', 'loc': 0.7,'delay': 0, 'conds':{'popLabel': 'Traub_pop'}})
netParams.addStimTargetParams('Input_2 -> S', {'source':'Input_2', 'sec':'dend', 'loc': 1.0,'delay': 0, 'conds':{'popLabel': 'Traub_pop'}})
netParams.addStimTargetParams('Input_3 -> S', {'source':'Input_3', 'sec':'soma', 'loc': 0.1,'delay': 0, 'conds':{'popLabel': 'Traub_pop'}})
 
 
 
#simConfig
simConfig = specs.SimConfig() 
simConfig.duration = 70
simConfig.dt = 0.025
simConfig.verbose = False
simConfig.recordTraces = {'V_Soma': {'sec':'comp_1', 'loc':0.5, 'var':'v'}}
simConfig.recordStep = 0.5
simConfig.filename = 'model_output'
simConfig.savePickle = True

simConfig.addAnalysis('plotRaster', True)
simConfig.addAnalysis('plotTraces', {'include': [0]})
simConfig.addAnalysis('plot2Dnet', True)

sim.createSimulateAnalyze(netParams, simConfig)

