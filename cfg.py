"""
    params.py
    cfg is an object containing a set of simulation configurations using a standardized structure
    Contributors: salvadordura@gmail.com
    """

from netpyne import specs

cfg = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

###############################################################################
# SIMULATION CONFIGURATION
###############################################################################

# Simulation parameters
cfg.duration = 0.5*1e3 # Duration of the simulation, in ms
cfg.dt = 0.05 # Internal integration timestep to use
cfg.seeds = {'conn': 1, 'stim': 1, 'loc': 1} # Seeds for randomizers (connectivity, input stimulation and cell locations)
cfg.createNEURONObj = 1  # create HOC objects when instantiating network
cfg.createPyStruct = 1  # create Python structure (simulator-independent) when instantiating network
cfg.verbose = 0 # Whether to write diagnostic information on events
cfg.hParams = {'celsius': 34, 'v_init': -65}  # set celsius temp

# Recording
cfg.recordTraces = {'V_soma': {'sec': 'soma', 'loc': 0.5, 'var': 'v'}}

cfg.recordStims = False  # record spikes of cell stims
cfg.recordStep = 0.1 # Step size in ms to save data (eg. V traces, LFP, etc)

# Saving
cfg.simLabel = 'M1_cell'
cfg.saveFolder = 'data'
cfg.savePickle = False # save to pickle file
cfg.saveJson = True # save to json file
cfg.saveMat = False # save to mat file
cfg.saveDataInclude = ['simData', 'simConfig', 'netParams']
cfg.gatherOnlySimData = False

# Analysis and plotting
#cfg.addAnalysis('plotRaster', True) # Whether or not to plot a raster
cfg.analysis['plotTraces'] = {'include': [0], 'saveFig': True, 'showFig': False} # plot recorded traces for this list of cells

# batch parameters


#------------------------------------------------------------------------------
# Synapses
#------------------------------------------------------------------------------
cfg.synWeightFractionEE = [1.0, 0.1] # E->E AMPA to NMDA ratio
cfg.synWeightFractionEI = [1.0, 0.1] # E->I AMPA to NMDA ratio
cfg.synWeightFractionSOME = [1.0, 7.5] # SOM -> E GABAASlow to GABAB ratio

#---------------#---------------------------------------------------------------
# NetStim inputs 
#------------------------------------------------------------------------------
cfg.addNetStim = 1

# netstim #cfg.NetStimEPT

cfg.NetStim1 = {'numStims': 1,'pop': ['PT_L5B'], 'cellRule': 'PT_full', 'secList': 'alldend', 'allSegs': True, \
 						'synMech': ['AMPA', 'NMDA'] , 'start': 300, 'interval': 1000/20.0, 'noise': 0.25, 'number': 1, 'loc': 0.5, 'weight': 0.005, 'delay': 0}



