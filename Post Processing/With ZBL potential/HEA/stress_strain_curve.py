#stress strain curve generator (from def1.txt files, from tensile tests)

import matplotlib.pyplot as plt
import numpy as np
import csv

files_to_analyze = ['NiCoCrFe_Tensile_Unirradiated.def1.txt', 'NiCoCrFe_Tensile_5KeV.def1.txt']


colors = ['g', 'b']  # Define colors for each file
labels = ['NiCoCrFe Unirradiated', 'NiCoCrFe 5KeV']  # Labels for the legend

for idx, def1_file in enumerate(files_to_analyze):
    results = []
    with open(def1_file, newline='') as file:
        reader = csv.reader(file, delimiter=' ')
        next(reader)  # Skip header row.
        for row in reader:
            row2 = [float(i) for i in row]
            results.append(row2)

    results2 = np.transpose(results)
    plt.plot(results2[0], results2[3], '-o', label=labels[idx], color=colors[idx],
             lw=2, markersize=5, mec=colors[idx], mfc=colors[idx])

plt.xlabel('Strain', fontsize=16)
plt.ylabel('Stress (GPa)', fontsize=16)
plt.title('Stress versus Strain', fontsize=16)
plt.legend(fontsize=12)
plt.ylim(0, 20)
plt.xlim(-0.05, 0.25)
plt.show()
