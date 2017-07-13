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

b = createBatch({'sec':['soma', 'dend_5', 'apic_47'],'weight':[0.09, 0.03, 0.017],'loc':[0.1, 0.7, 0.2]})

runBatch(b, "test2")





