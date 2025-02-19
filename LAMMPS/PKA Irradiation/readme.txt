# Input script changelog

------------------------------------------------------------------------------------------------------------------

-------------------------------------
FOR PURE NI CRYSTAL                 |
-------------------------------------

# Attempt 2

- A central atom is picked near the center of the simulation cell now to act as the PKA recoil atom. 

- The velocity of the PKA for 5KeV energy was calculated manually as 1282 angstroms per picosecond (With KE=(1/2)mv^2) and will 
  be entered as such, in the z axis direction 

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

- Velocities were also removed from dump files for speed + storage improvements

- Dump is now done every 1000 cycles

--------------------------------------
# Attempt 5 (Fixing issue with writing a .lmp file for further downstream tensile tests and analysis) 

- Simulation writes to a Ni_irradiated_5KeV.lmp file after simulation finishes (as measured by simulation time elapsed > 25ps)
  and then force quits

--------------------------------------
  
# Attempt 6 (New interatomic potential)

- The NiCoCrFe IAP is now used for PKA 

--------------------------------------
# Attempt 7 (New ZBL splined interatomic potential)

- The 2021 IAP is now used with ZBL splining for cascade collisions
- neighbor bins and neigh_modify also changed to latest NiCoCrFe irradiation (Attempt 8)'s values

--------------------------------------




------------------------------------------------------------------------------------------------------------------



-------------------------------------
FOR NiCoCrFe ALLOY                  |
-------------------------------------

- PKA was done along Z (default) and X axis directions 

- Attempt #1 -#3 are PKA along the Z-axis 

- Attempt #4 and #5 are PKA along the X-axis

- Attempt #6 and #7 are PKA along the XY-direction

- Attempt #8 is using the new updated 2021 potential (with ZBL splining) along the Z-axis 
