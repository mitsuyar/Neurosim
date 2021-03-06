"""
params.py 

netParams is an object containing a set of network parameters using a standardized structure

simConfig is an object containing a set of simulation configurations using a standardized structure

Contributors: salvadordura@gmail.com
"""

from netpyne import specs
from neuron import h,gui

netParams = specs.NetParams()   # object of class NetParams to store the network parameters

try:
	from __main__ import cfg  # import SimConfig object with params from parent module
except:
	from cfg import cfg

#------------------------------------------------------------------------------#
# M1 6-LAYER ynorm-BASED MODEL
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# NETWORK PARAMETERS
#------------------------------------------------------------------------------

# General network parameters
netParams.scale = 1 # Scale factor for number of cells
netParams.sizeX = 30 # x-dimension (horizontal length) size in um
netParams.sizeY = 1350 # y-dimension (vertical height or cortical depth) size in um
netParams.sizeZ = 30 # z-dimension (horizontal depth) size in um

## General connectivity parameters
netParams.scaleConnWeight = 1.0 # Connection weight scale factor (default if no model specified)
netParams.scaleConnWeightModels = {'Izhi2007b': 0.01, 'HH_reduced': 0.005, 'HH_full': 0.005}  # scale conn weight factor for each cell model
netParams.scaleConnWeightNetStims = 1.0 #0.5  # scale conn weight factor for NetStims
netParams.defaultDelay = 5.0 # default conn delay (ms)
netParams.propVelocity = 500.0 # propagation velocity (um/ms)
netParams.probLambda = 100.0  # length constant (lambda) for connection probability decay (um)



# Cell parameters
SimpSecD = {}
SimpSecD['alldend'] = ['Adend2'] # ['Adend1', 'Adend2', 'Adend3', 'Bdend']
SimpSecD['apicdend'] = ['Adend1', 'Adend2', 'Adend3']
SimpSecD['perisom'] = ['soma']

## PT cell params (6-comp)
cellRule = netParams.importCellParams(label='PT_6comp',conds={'cellType': 'PT', 'cellModel': 'HH_reduced'},
  fileName='cells/SPI6.py', cellName='SPI6')
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -75.0413649414 
for k in ['alldend', 'apicdend','perisom']: cellRule['secLists'][k] = SimpSecD[k]

## PT cell params (full)
cellRule = netParams.importCellParams(label='PT_full',conds={'cellType': 'PT', 'cellModel': 'HH_full'},
  fileName='cells/PTcell.hoc', cellName='PTcell', cellArgs = [0, 0,0])
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -70.0432010302
cellRule['secLists']['perisom'] = ['soma']
cellRule['secLists']['perisom'].extend([sec for sec in cellRule.secs if 'dend' in sec])  # soma+basal  
cellRule['secLists']['alldend'] = [sec for sec in cellRule.secs if ('dend' in sec or 'apic' in sec)] # basal+apical
cellRule['secLists']['apicdend'] = [sec for sec in cellRule.secs if ('apic' in sec)] # basal+apical
cellRule['secLists']['spiny'] = [sec for sec in cellRule['secLists']['alldend'] if sec not in ['apic_0', 'apic_1']]


## create list of populations, where each item contains a dict with the pop params
netParams.popParams['PT5B'] =	{'cellModel':'HH_full', 'cellType':'PT', 'numCells':1}


# Synaptic mechanism parameters
netParams.synMechParams['AMPA'] = {'mod':'MyExp2SynBB','tau1':0.05,'tau2':5.3,'e':0}
netParams.synMechParams['NMDA'] = {'mod':'MyExp2SynNMDABB','tau1NMDA':15,'tau2NMDA':150,'e':0}
netParams.synMechParams['GABAA'] = {'mod':'MyExp2SynBB','tau1':0.07,'tau2':18.2,'e':-80}
netParams.synMechParams['GABAASlow'] = {'mod':'MyExp2SynBB','tau1':2,'tau2':100,'e':-80}
netParams.synMechParams['GABAASlowSlow'] = {'mod':'MyExp2SynBB','tau1':200,'tau2':400,'e':-80}
netParams.synMechParams['GABAB'] = {'mod':'GABAB'}

ESynMech = ['AMPA', 'NMDA'] 
ISlowSynMech = ['GABAASlow','GABAB']
IFastSynMech = ['GABAA']

# Connectivity rules/params
synWeightFraction = [0.9, 0.1]


#------------------------------------------------------------------------------
## Subcellular connectivity (synaptic distributions)
#------------------------------------------------------------------------------
subcell = 0

if subcell:
	# load 1d and 2d density maps
	import numpy
	lenX = 10
	lenY = 30
	maxRatio = 15

	file1d = 'radial_scracm18_BS0284_memb_BS0477_morph.dat'
	data1d = numpy.loadtxt(file1d)
	map1d = []
	for jj in range(lenY):
		map1d.append(data1d[jj])

	fixedSomaY =-735
	spacing = 50
	gridX = range(-spacing*lenX/2, spacing*lenX/2, spacing)
	gridY = range(0, -spacing*lenY, -spacing) # NEURON's axis for cortical depth goes from 0 (pia) to -cfg.sizeY (WM)

	netParams.subConnParams['bg->PT'] = {
		'preConds': {'cellModel': 'NetStim'}, 
		'postConds': {'popLabel': 'PT5B', 'cellModel': 'HH_full'},  
		'sec': 'spiny',
		'groupSynMechs': ['AMPA', 'NMDA'], 
		'density': {'type': '1Dmap', 'gridX': None, 'gridY': gridY, 'gridValues': map1d, 'fixedSomaY': fixedSomaY}} 


#------------------------------------------------------------------------------
# NetStim inputs
#------------------------------------------------------------------------------
if cfg.addNetStim:

    for key in [k for k in dir(cfg) if k.startswith('NetStim')]:
    	params = getattr(cfg, key, None)
        numStims, pop, cellRule, secList, allSegs, synMech, start, interval, noise, number, loc, weight, delay = \
        [params[s] for s in 'numStims', 'pop', 'cellRule', 'secList', 'allSegs', 'synMech', 'start', 'interval', 'noise', 'number', 'loc', 'weight', 'delay']

        cfg.analysis['plotTraces']['include'].append((pop,0))

        if not isinstance(secList, list):
            secList = list(netParams.cellParams[cellRule]['secLists'][secList])

        segs = []
        
        # new addition to M1 code from here
        
    excludeSecs = ['axon']

    if not segs:
        secs = []
        locs = []
        for secName,sec in netParams.cellParams[rule]['secs'].iteritems():
            if secName not in excludeSegs:
                nseg = sec['geom']['nseg']
                for iseg in range(nseg):
                secs.append(secName)
                locs.append((iseg+1)*(1.0/(nseg+1)))
        
                

        if synMech == ESynMech:
            wfrac = cfg.synWeightFractionEE
        elif synMech == ISlowSynMech:
            wfrac = cfg.synWeightFractionSOME
        else:
            wfrac = [1.0]

        netParams.popParams[key] = {'cellModel': 'NetStim', 'numCells': numStims, 'rate': 1000.0/interval, 'noise': noise, 'start': start, 'number': number}
        
        netParams.connParams[key] = { 
                    'preConds': {'pop': key}, 
                    'postConds': {'pop': pop},
                    'synMech': synMech,
                    'weight': weight, 
                    'synWeightFraction': wfrac,
                    'delay': delay,
                    'synsPerConn': 1,
                    'sec': secList,
                    'loc': loc}
        
        netParams.subConnParams[key] = {
                    'preConds': {'pop': key}, 
                    'postConds': {'pop': pop},  
                    'sec': secList, 
                    'density': 'uniform'} 
