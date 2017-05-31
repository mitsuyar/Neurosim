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

createBatch([{'label': 'sec',    'values': ['soma', 'dend_5', 'apic_47']},{'label': 'weight', 'values': [0.0009, 0.003, 0.0017]},{'label':'loc', 'values':[0.5, 0.8, 0.3]}])

runBatch(b,test)


  #EXAMPLE
# Create Batch object
#b = Batch(netParamsFile='M1_cell.py')


# Add params
#b.params.append({'label': 'sec',    'values': ['soma', 'dend_5', 'apic_47']})
#b.params.append({'label': 'weight', 'values': [0.0004, 0.001, 0.0015]})


# Setup

            #b.batchLabel = 'batch1'
            #b.saveFolder = '../data/'+b.batchLabel
            #b.method = 'grid'
            #b.runCfg = {'type': 'mpi',
            #'script': 'init.py',
            #'skip': True}

# run batch
            #b.run()


