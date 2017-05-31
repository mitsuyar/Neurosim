"""
batch.py 

Batch simulation for M1 model using NetPyNE

Contributors: salvadordura@gmail.com
"""
from netpyne.batch import Batch



def createBatch(params):
    # Create Batch object
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

createBatch({'sec':['soma', 'dend_5', 'apic_47'],'weight':[0.0009, 0.003, 0.0017],'loc':[0.5, 0.8, 0.3]})

runBatch(b,test)





