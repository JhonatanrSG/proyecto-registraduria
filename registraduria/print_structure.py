import os

def export_directory_structure(startpath, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write(f'{indent}{os.path.basename(root)}/\n')
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f.write(f'{subindent}{file}\n')

# Define the path to the project directory and the output file
project_path = '.'
output_file = 'directory_structure.txt'

# Export the directory structure to a text file
export_directory_structure(project_path, output_file)

print(f"Directory structure has been exported to {output_file}")