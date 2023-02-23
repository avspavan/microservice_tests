# this code is a template to check if a python based microservice has some end points - but assumes dependency on flask and django
import re

# Define the regular expression pattern to search for Flask route decorators
flask_route_pattern = re.compile(r'@app.route\((.*)\)')

# Open the Python file containing the Flask microservice source code
with open('app.py', 'r') as f:
    source_code = f.read()

# Find all occurrences of Flask route decorators in the source code
flask_routes = re.findall(flask_route_pattern, source_code)

# Extract the endpoints from the Flask route decorators
endpoints = []
for route in flask_routes:
    endpoint = route.split(',')[0].strip("'")
    endpoints.append(endpoint)

# Print the available endpoints
print(endpoints)
