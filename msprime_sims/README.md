This directory contains scripts and files for assessing fitted model parameter bias. 
- sim.slr launches a script (sim.sh) that generates 50 simulated opfs from parameters specified in msp_pan.py
- remaining scripts run a deterministic analysis using the beta epsilon model on each of the simulations

NOTE: sim.sh requries a conda environment (msprime) to run. Make sure you are in bash on the command line before 
launching sim.slr. If not, type "bash" on command line. 
