# this uses Radon library. this is a sample from Radon tutorial. 
import os
import radon

# Define the directory path to the microservice
directory_path = '/path/to/microservice'

# Get the list of Python files in the microservice directory
python_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.py')]

# Initialize empty lists for the raw metrics and Cyclomatic Complexity (McCabe)
raw_metrics = []
cc = []

# Loop over each Python file in the microservice directory
for file_path in python_files:
    # Get the raw metrics for the file
    raw_metrics.append(radon.raw.open(file_path).raw_metrics)
    
    # Get the Cyclomatic Complexity (McCabe) for the file
    cc.append(radon.complexity.cc_visit(file_path))

# Print the results
print('Raw Metrics:', raw_metrics)
print('Cyclomatic Complexity:', cc)
