

import utils
import json
import matplotlib.pyplot as plt




def epsp(params, data):
   
    
    plt.style.use('ggplot')
    Lepsp = []
    Loclist = []
    epsplist= []
    for key, d in data.iteritems():
        vsoma = d['simData']['V_soma']['cell_0']
        epsp = max(vsoma[2000:6000]) - vsoma[1999]
        print d['paramValues']
        print  epsp
        epsplist.append(epsp)
        Lepsp.append({str(d['paramValues']): epsp})
        Loclist.append(d['paramValues'][3])
    


    plt.figure()
    plt.plot(Loclist, epsplist, 'o', markersize = 3)
    plt.xlabel("Location on Dendrites")
    plt.ylabel("Somatic EPSP amplitude")
    plt.xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    plt.savefig('%s/%s/%s_epsp.png' % (dataFolder, batchLabel, batchLabel))

    plt.show



    
    filename = '%s/%s/%s_epsp.json' % (dataFolder, batchLabel, batchLabel)
    with open(filename, 'w') as fileObj:
        json.dump(Lepsp, fileObj)

    





if __name__ == '__main__':

    dataFolder = '../sim/data'
    batchLabel = 'Data2'
    loadFromFile = 0
    saveToFile = 1
    
    filename = '%s/%s/%s_allData.json' % (dataFolder, batchLabel, batchLabel)

    
    params, data = utils.readBatchData(dataFolder, batchLabel) 
    epsp(params, data)

