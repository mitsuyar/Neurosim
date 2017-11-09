"""
batch.py 

Batch simulation for M1 model using NetPyNE

Contributors: salvadordura@gmail.com
"""
from netpyne.batch import Batch
import numpy as np
from netpyne import specs




"""
params[('NetStimEPT', 'numStims')] = [1]
params[('NetStimEPT', 'weight')] = [0.03, 0.04, 0.05]
params[('NetStimEPT', 'secList')] = ['basal'  #'alldend', 'apic',]
params[('NetStimEPT', 'loc')] = [0.3, 0.6, 0.9]
"""






#runBatch(b, "Data3")


#Exploring all segs


#Define weightNormE function





"""
def createBatch(params):
    b = Batch(netParamsFile='M1_detailed.py', groupedParams=groupedParams)
    for k,v in params.iteritems():
        b.params.append({'label': k, 'values': v})
    return b
"""
#Define batchrun
def runBatch(b, label):
    b.batchLabel = label
    b.saveFolder = 'data/'+b.batchLabel
    b.method = 'grid'
    b.runCfg = {'type': 'mpi',
        'script': 'init.py',
            'skip': True}
    b.run()

"""
    initCfg = {}
    initCfg['duration'] = 1.0*1e3
    initCfg[('analysis','plotTraces','timeRange')] = [0, 1000]
    initCfg['weightNorm'] = False
    initCfg['stimSubConn'] = False
    initCfg[('NetStim1', 'synMech')] = ['AMPA','NMDA']
    initCfg[('NetStim1','synMechWeightFactor')] = [0.5,0.5]
    initCfg[('NetStim1', 'start')] = 300
    initCfg[('NetStim1', 'interval')] = 1000/20.0
    initCfg[('NetStim1', 'noise')] = 0.25
    initCfg[('NetStim1', 'number')] = 1
    initCfg[('NetStim1', 'delay')] = 0
    #initCfg[('GroupNetStimW1', 'pop')] = 'None'
    initCfg['addIClamp'] = 0
"""


#weights=list(np.arange(0.01, 0.2, 0.01)/100.0))
#b = createBatch(params)
#b = Batch(params=params, netParamsFile='netParams_cell.py', cfgFile='cfg_cell.py', initCfg=initCfg, groupedParams=groupedParams)



secs = []
locs = []
pops=['PT_L5B']
weights = [0.01]

def weightNormE(pops=['PT_L5B'],
                segs = None, allSegs = True, rule = 'PT_full', weights= [0.01]):
    # Add params
    from cfg import cfg
    from M1_detailed import netParams
    excludeSegs = ['axon']
    if not segs:
        for secName,sec in netParams.cellParams[rule]['secs'].iteritems():
            if secName not in excludeSegs:
                if allSegs:
                    nseg = sec['geom']['nseg']
                    for iseg in range(nseg):
                        secs.append(secName)
                        locs.append((iseg+1)*(1.0/(nseg+1)))
                else:
                    secs.append(secName)
                    locs.append(0.5)



weightNormE(pops= pops,
                segs = None, allSegs = True, rule = 'PT_full', weights= [0.01])

params = specs.ODict()
params[('NetStim1', 'pop')] = pops
params[('NetStim1', 'sec')] = secs
params[('NetStim1', 'loc')] = locs
params[('NetStim1', 'weight')] = weights
groupedParams = [('NetStim1', 'sec'), ('NetStim1', 'loc')]

b = Batch(params=params, netParamsFile='M1_detailed.py', cfgFile='cfg.py',groupedParams=groupedParams)






    



runBatch(b,"Data 4")



