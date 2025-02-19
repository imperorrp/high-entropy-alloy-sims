# Python script to execute Tensile Test scripts
from mpi4py import MPI
from lammps import lammps 

lmp = lammps() 

def execute_tensile_test(num_threads, input_file, output_stress_file, output_dump_file, output_lmp_file):

    lmp = lammps() 

    lmp.command("variable nthreads equal " + str(num_threads))
    lmp.command("variable inputfile string " + input_file)
    lmp.command("variable outputfile_stress string " + output_stress_file) 
    lmp.command("variable dumpfile string " + output_dump_file)
    lmp.command("variable outputfile_lmp string " + output_lmp_file)

    print("LAMMPS Version: ", lmp.version())
    lmp.file("NiCoCrFe_Tensile_Test_Unirradiated.in")
    print("Simulation complete.")

# Example usage:
num_threads = 4
input_file = "NiCoCrFe_relaxed.lmp"
output_stress_file = "NiCoCrFe_Tensile_Unirradiated.def1.txt"
output_dump_file = "dump.NiCoCrFe_Tensile_Unirradiated_*.dump"
output_lmp_file = "NiCoCrFe_unirradiated_Strained.lmp"

execute_tensile_test(num_threads, input_file, output_stress_file, output_dump_file, output_lmp_file)





# Enter number of threads to use:
num_threads = 4
lmp.command("variable nthreads equal " + str(num_threads))
# Enter lammps file to be read 
input_file = "NiCoCrFe_relaxed.lmp"
lmp.command("variable inputfile string " + input_file)
# Enter name of output stress/strain file
output_stress_file = "NiCoCrFe_Tensile_Unirradiated.def1.txt"
lmp.command("variable outputfile_stress string " + output_stress_file) 
# Enter name of output dump files
output_dump_file = "dump.NiCoCrFe_Tensile_Unirradiated_*.dump"
lmp.command("variable dumpfile string " + output_dump_file)
# Enter name of output .lmp file
output_lmp_file = "NiCoCrFe_unirradiated_Strained.lmp"
lmp.command("variable outputfile_lmp string " + output_lmp_file)
# get and print numerical version code
print("LAMMPS Version: ", lmp.version())
lmp.file("NiCoCrFe_Tensile_Test_Unirradiated.in")
print("Simulation complete.")