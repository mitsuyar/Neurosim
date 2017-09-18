"""
batch.py 

Batch simulation for M1 model using NetPyNE

Contributors: salvadordura@gmail.com
"""
from netpyne.batch import Batch



def createBatch(params):
    b = Batch(netParamsFile='M1_cell.py')
    for k,v in params.iteritems():
        b.params.append({'label': k, 'values': v})
    return b

def runBatch(b, label):
    b.batchLabel = label
    b.saveFolder = 'data/'+b.batchLabel
    b.method = 'grid'
    b.runCfg = {'type': 'mpi',
        'script': 'init.py',
            'skip': True}
    b.run()

params = {}

params[('NetStimEPT', 'numStims')] = [50, 100, 150]
params[('NetStimEPT', 'weight')] = [0.001, 0.002, 0.003]
params[('NetStimEPT', 'secList')] = ['alldend', 'apic', 'basal']
params[('NetStimEPT', 'loc')] = [0.3, 0.6, 0.9]


b = createBatch(params)



runBatch(b, "Data2")





