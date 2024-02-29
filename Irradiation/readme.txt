# Attempt Modification History 

-------------------------------------
# Attempt 2

- A central atom is picked near the center of the simulation cell now to act as the PKA recoil atom. 

- The velocity of the PKA for 5KeV energy was calculated manually as 1282 angstroms per picosecond and will be entered as 
  such, in the z axis direction 

- The timestep is also being varied to speed up the simulation, to 0.01. Number of steps will thus be 2500 to simulate 25ps of time. 

- Dumps will be made every 100 steps. 

- Number of threads used was set to 4 for speeding up simulation

---------------------------------------
# Attempt 3

- Variable timesteps will be used (smaller at first as PKA atom will be moving fast) to ensure no atom moves further than 
  0.02 angstroms (as mentioned in referenced paper)

- Boundary atoms will be fixed (as seen in examples)

- Forces on atoms were removed from the dump files

--------------------------------------
# Attempt 4 (Performance upgrades made)

- LAMMPS was uninstalled and another stable release compatible with MSMPI was installed for multiprocessor usage

- Velocities were also removed from dump files

- Dump is now done every 1000 cycles

--------------------------------------
# Attempt 5 (Fixing issue with writing a .lmp file for further downstream tensile tests and analysis) 

- Simulation should write to a Ni_irradiated_5KeV.lmp file after simulation finishes
  instead of quitting before doing so 
