

import utils
import json
import matplotlib.pyplot as plt




def epsp(params, data):
    
    plt.style.use('ggplot')
    Lepsp = []
    for key, d in data.iteritems():
        vsoma = d['simData']['V_soma']['cell_0']
        epsp = max(vsoma[2000:3000]) - vsoma[1999]
        print d['paramValues']
        print  epsp
        Lepsp.append({str(d['paramValues']): epsp})
    print Lepsp
    

    
    filename = '%s/%s/%s_epsp.json' % (dataFolder, batchLabel, batchLabel)
    with open(filename, 'w') as fileObj:
        json.dump(Lepsp, fileObj)

    





if __name__ == '__main__':

    dataFolder = '../sim/data'
    batchLabel = 'test2'
    loadFromFile = 0
    saveToFile = 1
    
    filename = '%s/%s/%s_allData.json' % (dataFolder, batchLabel, batchLabel)

    
    params, data = utils.readBatchData(dataFolder, batchLabel) 
    epsp(params, data)

