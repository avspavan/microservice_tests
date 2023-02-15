# this is for cpp based microservice. 
import os
import subprocess

# Define the directory path to the microservice
directory_path = '/path/to/microservice'

# Get the list of C++ files in the microservice directory
cpp_files = []
for subdir, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith('.cpp'):
            cpp_files.append(os.path.join(subdir, file))

# Initialize empty list for the complexity metrics
complexity_metrics = []

# Loop over each C++ file in the microservice directory
for cpp_file in cpp_files:
    # Use cppcheck to analyze the file and get the complexity metrics
    result = subprocess.run(["cppcheck", "--enable=style,performance,portability", cpp_file], capture_output=True, text=True)
    # Extract the complexity metrics from the cppcheck output
    lines = result.stdout.split('\n')
    complexity = [int(line.split()[1]) for line in lines if line.startswith('Cppcheck:') and 'complexity' in line]
    complexity_metrics.append(complexity[0] if complexity else 0)

# Calculate the average complexity of the microservice
avg_complexity = sum(complexity_metrics) / len(complexity_metrics)

# Print the results
print('Average complexity of the microservice:', avg_complexity)
