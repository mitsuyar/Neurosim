from netpyne import specs,sim
netParams = specs.NetParams()

#popParams defined 
netParams.addPopParams('S', {'cellType': 'S', 'numCells':1, 'cellModel': 'HH'})
netParams.addPopParams('M',{'cellType': 'M', 'numCells':1, 'cellModel':'HH'})



#cellRules for I pop
cellRule = {'conds': {'popLabel': 'S'}, 'secs':{}}
cellRule['secs']['soma'] = {'geom':{}, 'mechs':{}}
cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.13, 'gkbar': 0.0321, 'gl': 0.002, 'el':-65}
cellRule['secs']['dend'] = {'geom' : {}, 'topol':{}, 'mechs':{}}
cellRule['secs']['dend']['geom']= {'diam': 10, 'L': 15, 'Ra': 120.0, 'cm': 1}
cellRule['secs']['dend']['mechs']['pas'] = {'g': 0.0000321, 'e': -70 }
cellRule['secs']['dend']['topol'] = {'parentSec': 'soma', 'parentX':1.0, 'childX': 0}
netParams.addCellParams('Srule', cellRule)

cellRule = {'conds':{'popLabel': 'M'}, 'secs':{}}
cellRule['secs']['soma'] = {'geom':{}, 'mechs':{}}
cellRule['secs']['dend'] = {'geom' : {}, 'topol':{}, 'mechs':{}}
cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.13, 'gkbar': 0.0321, 'gl': 0.002, 'el':-65}
cellRule['secs']['dend']['geom']= {'diam': 10, 'L': 15, 'Ra': 120.0, 'cm': 1}
cellRule['secs']['dend']['mechs']['pas'] = {'g': 0.0000321, 'e': -70 }
cellRule['secs']['dend']['topol'] = {'parentSec': 'soma', 'parentX':1.0, 'childX': 0}
netParams.addCellParams('Mrule', cellRule)
#SynMech
netParams.addSynMechParams('exc', {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 5.0, 'e': 0})

netParams.addConnParams('S->M',{'preConds': {'popLabel': 'S'},'postConds': {'popLabel': 'M'}, 'delay': 5,'sec':'dend','loc':1.0,'synMech':'exc'}) 

netParams.addStimSourceParams('Input_1',{'type': 'IClamp', 'delay': 5, 'dur': 10, 'amp': 10})
netParams.addStimSourceParams('Input_2',{'type': 'IClamp', 'delay': 5, 'dur': 10, 'amp': 10})
netParams.addStimTargetParams('Input_1 -> S', {'source':'Input_1', 'sec':'dend', 'loc': 1.0,'delay': 0, 'conds':{'popLabel': 'S'}})
netParams.addStimTargetParams('Input_2 -> S', {'source':'Input_2', 'sec':'dend', 'loc': 1.0,'delay': 0, 'conds':{'popLabel': 'S'}})


#simConfig
simConfig = specs.SimConfig() 
simConfig.duration = 70
simConfig.dt = 0.025
simConfig.verbose = False
simConfig.recordTraces = {'V_Soma': {'sec':'soma', 'loc':0.5, 'var':'v', 'popLabel':'S'}}
simConfig.recordStep = 0.1
simConfig.filename = 'model_output'
simConfig.savePickle = False

simConfig.addAnalysis('plotRaster', True)
simConfig.addAnalysis('plotTraces', {'include': [0]})
simConfig.addAnalysis('plot2Dnet', True)

sim.createSimulateAnalyze(netParams, simConfig)




