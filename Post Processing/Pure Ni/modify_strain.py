# modify strain from def1 file (only for Ni_Tensile_5KeV.def1.txt due to incorrect format when generated)

# Define the input and output file names
input_file = 'Ni_Tensile_5KeV.def1.txt'
output_file = 'modified_Ni_Tensile_5KeV.def1.txt'

# Read the input file and modify the rows
with open(input_file, 'r') as file:
    lines = file.readlines()

# Modify the rows, starting from the second row (index 1)
modified_lines = [lines[0]]  # Keep the header row unchanged
modified_lines.append(lines[1])
for idx, line in enumerate(lines[2:], start=1):
    new_number = '{:.4f}'.format(idx * 0.0002)
    modified_line = line.split(' ')
    modified_line[0] = new_number
    modified_lines.append(' '.join(modified_line))  


# Write the modified rows to a new file
with open(output_file, 'w') as file:
    file.writelines(modified_lines)

print(f"Modified file '{output_file}' has been created.")


