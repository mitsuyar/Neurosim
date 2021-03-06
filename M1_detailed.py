"""
params.py 

netParams is an object containing a set of network parameters using a standardized structure

Contributors: salvadordura@gmail.com
"""

from netpyne import specs
from neuron import h,gui
import pickle

netParams = specs.NetParams()# object of class NetParams to store the network parameters

try:
    from __main__ import cfg  # import SimConfig object with params from parent module
except:
    from cfg import cfg

###############################################################################
#
# M1 6-LAYER ynorm-BASED MODEL
#
###############################################################################

###############################################################################
# NETWORK PARAMETERS
###############################################################################

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
"""
## IT cell params (full)
cellRule = netParams.importCellParams(label='IT_full', conds={'cellType': 'IT', 'cellModel': 'HH_full'},
  fileName='cells/ITcell.hoc', cellName='ITcell', cellArgs = [0, 0,0])
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -70.0432010302

## IT cell params (6-comp)
cellRule = netParams.importCellParams(label='IT_6comp',conds={'cellType': 'IT', 'cellModel': 'HH_reduced'},
  fileName='cells/CSTR6.py', cellName='CSTR6')
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -75.0413649414 
for k in ['alldend', 'apicdend','perisom']: cellRule['secLists'][k] = SimpSecD[k]
"""
"""## PT cell params (6-comp)
cellRule = netParams.importCellParams(label='PT_6comp',conds={'cellType': 'PT', 'cellModel': 'HH_reduced'},
  fileName='cells/SPI6.py', cellName='SPI6')
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -75.0413649414 
for k in ['alldend', 'apicdend','perisom']: cellRule['secLists'][k] = SimpSecD[k]
"""
## PT cell params (full)
cellRule = netParams.importCellParams(label='PT_full',conds={'cellType': 'PT', 'cellModel': 'HH_full'},
  fileName='cells/PTcell.hoc', cellName='PTcell', cellArgs = [0, 0,0])
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -70.0432010302
cellRule['secLists']['perisom'] = ['soma']
cellRule['secLists']['perisom'].extend([sec for sec in cellRule.secs if 'dend' in sec])  # soma+basal  
cellRule['secLists']['alldend'] = [sec for sec in cellRule.secs if ('dend' in sec or 'apic' in sec)] # basal+apical
cellRule['secLists']['apicdend'] = [sec for sec in cellRule.secs if ('apic' in sec)] # basal+apical
cellRule['secLists']['spiny'] = [sec for sec in cellRule['secLists']['alldend'] if sec not in ['apic_0', 'apic_1']]
"""
## CT cell params (6-comp)
cellRule = netParams.importCellParams(label='CT_6comp',conds={'cellType': 'CT', 'cellModel': 'HH_reduced'},
  fileName='cells/CSTR6.py', cellName='CSTR6')
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -75.0413649414 
for k in ['alldend', 'apicdend','perisom']: cellRule['secLists'][k] = SimpSecD[k]

## SOM cell params
cellRule = netParams.importCellParams(label='SOM', conds={'cellType': 'SOM','cellModel':'HH_reduced'},
  fileName='cells/LTS1.py', cellName='LTS1', cellArgs=[0,0,0,0,0])

## PV cell params
cellRule = netParams.importCellParams(label='PV', conds={'cellType':'PV','cellModel':'HH_reduced'}, 
  fileName='cells/BAS1.py', cellName='BAS1', cellArgs=[0,0,0,0,0])

"""
## create list of populations, where each item contains a dict with the pop params
#netParams.addPopParams('CT_L6',		{'cellModel':'HH_reduced',	'cellType':'CT',	'ynormRange':[0.77,1.0],	'density':40e3})
#netParams.addPopParams('IT_L6',		{'cellModel':'HH_reduced',	'cellType':'IT',	'ynormRange':[0.77,1.0],	'density':40e3})
#netParams.addPopParams('SOM_L6',	{'cellModel':'HH_reduced',	'cellType':'SOM',	'ynormRange':[0.77,1.0],	'density':10e3})
#netParams.addPopParams('PV_L6',		{'cellModel':'HH_reduced',	'cellType':'PV',	'ynormRange':[0.77,1.0],	'density':10e3})
netParams.addPopParams('PT_L5B',	{'cellModel':'HH_full',	 'cellType':'PT', 'numCells':1,	'ynormRange':[0.52,0.77]})
#netParams.addPopParams('IT_L5B',	{'cellModel':'HH_full',		'cellType':'IT',	'ynormRange':[0.52,0.77],	'density':40e3})
#netParams.addPopParams('IT_L5A',	{'cellModel':'HH_full',		'cellType':'IT',	'ynormRange':[0.41,0.52],	'density':80e3})
#netParams.addPopParams('SOM_L5',	{'cellModel':'HH_reduced',	'cellType':'SOM',	'ynormRange':[0.31,0.77],	'density':10e3})
#netParams.addPopParams('PV_L5',		{'cellModel':'HH_reduced',	'cellType':'PV',	'ynormRange':[0.31,0.77],	'density':10e3})
#netParams.addPopParams('IT_L4',		{'cellModel':'HH_reduced',	'cellType':'IT',	'ynormRange':[0.31, 0.41],	'density':80e3})
#netParams.addPopParams('IT_L23',	{'cellModel':'HH_reduced',	'cellType':'IT',	'ynormRange':[0.12, 0.31],	'density':80e3})
#netParams.addPopParams('SOM_L23',	{'cellModel':'HH_reduced',	'cellType':'SOM',	'ynormRange':[0.12,0.31],	'density':10e3})
#netParams.addPopParams('PV_L23',	{'cellModel':'HH_reduced',	'cellType':'PV',	'ynormRange':[0.12,0.31],	'density':10e3})

# Synaptic mechanism parameters
netParams.addSynMechParams('AMPA', {'mod':'MyExp2SynBB','tau1':0.05,'tau2':5.3,'e':0})
netParams.addSynMechParams('NMDA', {'mod':'MyExp2SynNMDABB','tau1NMDA':15,'tau2NMDA':150,'e':0})
netParams.addSynMechParams('GABAA', {'mod':'MyExp2SynBB','tau1':0.07,'tau2':18.2,'e':-80})
netParams.addSynMechParams('GABAASlow', {'mod':'MyExp2SynBB','tau1':2,'tau2':100,'e':-80})
netParams.addSynMechParams('GABAASlowSlow', {'mod':'MyExp2SynBB','tau1':200,'tau2':400,'e':-80})
netParams.addSynMechParams('GABAB', {'mod':'GABAB'})

ESynMech = ['AMPA', 'NMDA'] 
ISlowSynMech = ['GABAASlow','GABAB']
IFastSynMech = ['GABAA']


# Connectivity rules/params
synWeightFraction = [0.9, 0.1]
EtoPTweightFactor = 0.2
netParams.ItoIweight = 0.1

addBackground = 1

####################################################################################################
## Background inputs
####################################################################################################
"""
if addBackground:
	# Create populations of NetStims
	bgNoise = 0.5
	bgRates = {'CT': 10, 'IT': 10, 'PT': 10, 'PV': 10, 'SOM': 10}
 	for postType in ['CT', 'IT', 'PT', 'PV', 'SOM']:
	    bgPopParams = {'cellModel': 'NetStim', 'noise': bgNoise, 'rate': bgRates[postType], 'start':0}
        netParams.addPopParams('bg'+postType, bgPopParams)

	# Created conn rules between bg->E
	bgWeightsE = {'CT': 0.1, 'IT': 0.1, 'PT': 0.1, 'PV': 0.1, 'COM': 0.1}
	bgWeightsI = {'CT': 0.0, 'IT': 0.0, 'PT': 0.0, 'PV': 0.0, 'COM': 0.0}
  	for postType in ['CT', 'IT', 'PT']: # postsynaptic E cell types  		
  		for mech,sec,wt in zip(['AMPA','GABAA'], ['alldend','perisom'], [bgWeightsE[postType], bgWeightsI[postType]]):
  			netParams.addConnParams(params={'preConds': {'popLabel': 'bg'+postType}, 
	                                      'postConds': {'cellType': postType},
	                                      'sec':sec,
	                                      'synMech': mech,
	                                      'weight': wt,
	                                      'loc': 0.5,
	                                      'delay': 'max(defaultDelay, gauss(5,3))'})
                                          
"""
"""
    # Created conn rules between bg->I
  	for poty in ['PV', 'SOM']: # postsynaptic I cells
  		for mech,sec,wt in zip(['AMPA','GABAA'], ['alldend','perisom'], [bgWeightsE[postType], bgWeightsI[postType]]):
  			netParams.addConnParams(params={'preConds': {'popLabel': 'bg'+postType}, 
	                                      'postConds': {'cellType': postType},
	                                      'synMech': mech,
	                                      'weight': wt,
	                                      'loc': 0.5,
	                                      'delay': 'max(defaultDelay, gauss(5,3))'})  

"""

####################################################################################################
## Subcellular connectivity (synaptic distributions)
####################################################################################################   		

# # load 2d density maps
# import numpy
# lenX = 10
# lenY = 30
# somaY = -735
# spacing = 50
# maxRatio = 15
# file2d = 'density_scracm18_BS0284_memb_BS0477_morph.dat'
# data2d = numpy.loadtxt(file2d)
# map2d = [[None for _ in range(lenY)] for _ in range(lenX)] 
# for ii in range(lenX): 
# 	for jj in range(lenY):
# 		map2d[ii][jj] = data2d[ii*30+jj]
# gridX = range(-spacing*lenX/2, spacing*lenX/2, spacing)
# gridY = range(0, -spacing*lenY, -spacing) # NEURON's axis for cortical depth goes from 0 (pia) to -cfg.sizeY (WM)

# netParams.subConnParams['IT2->PT'] = {
# 	'preConds': {'popLabel': ['IT2']}, 
# 	'postConds': {'popLabel': 'PT5B'},  
# 	'sec': 'spiny',
# 	'groupSynMechs': ['AMPA', 'NMDA'], 
# 	'density': {'type': '2Dmap', 'gridX': gridX, 'gridY': gridY, 'gridValues': map2d, 'somaY': somaY}}

#Added from M1_cell
"""
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
"""
#------------------------------------------------------------------------------
# NetStim inputs
#------------------------------------------------------------------------------

if cfg.addNetStim:
    for key in [k for k in dir(cfg) if k.startswith('NetStim')]:
        params = getattr(cfg, key, None)
        numStims, pop, cellRule, secList, allSegs, synMech, start, interval, noise, number, loc, weight, delay = \
        [params[s] for s in 'numStims', 'pop', 'cellRule', 'secList', 'allSegs', 'synMech', 'start', 'interval', 'noise', 'number', 'loc', 'weight', 'delay']
        
        cfg.analysis['plotTraces']['include'].append((pop,0))
        
        #if not isinstance(secList, list):
        #secList = list(netParams.cellParams[cellRule]['secLists'][secList])
        
        segs = []

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
                    'sec': sec,
                    'density': 'uniform'}

