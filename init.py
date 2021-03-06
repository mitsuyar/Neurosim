"""
init.py

A modularized framework to develop and run large-scale network simulations. 
Built solely in Python with MPI support. 

Usage:
    python init.py # Run simulation, optionally plot a raster

MPI usage:
    mpiexec -n 4 nrniv -python -mpi main.py

Contributors: salvadordura@gmail.com
"""

from netpyne import sim
from neuron import h,gui
cfg, netParams = sim.readCmdLineArgs(simConfigDefault= 'cfg.py', netParamsDefault= 'M1_detailed.py')
 #M1_cell originally, test change rn


sim.initialize(
    simConfig=cfg, 
    netParams=netParams)  # create network object and set cfg and net params
sim.net.createPops()                  # instantiate network populations
sim.net.createCells()                 # instantiate network cells based on defined populations
sim.net.connectCells()                # create connections between cells based on params
sim.setupRecording()              # setup variables to record for each cell (spikes, V traces, etc)
sim.runSim()                      # run parallel Neuron simulation  
sim.gatherData()                  # gather spiking data and cell info from each node
sim.saveData()                    # save params, cell info and sim output to file (pickle,mat,txt,etc)
sim.analysis.plotData()               # plot spike raster


c=sim.net.cells
pt=next(cell for cell in c if cell.tags['cellType']=='PT')



