// this is to measure code complexity of JS microservice - uses escomplex git repo: https://github.com/escomplex/escomplex
// see the repo for more details
const fs = require('fs');
const escomplex = require('escomplex');

// Define the directory path to the microservice
const directoryPath = '/path/to/microservice';

// Get the list of JavaScript files in the microservice directory
const jsFiles = fs.readdirSync(directoryPath).filter(file => file.endsWith('.js'));

// Initialize empty lists for the metrics
const metrics = [];

// Loop over each JavaScript file in the microservice directory
jsFiles.forEach(file => {
  // Read the file and convert to a string
  const fileContent = fs.readFileSync(`${directoryPath}/${file}`, 'utf-8');
  
  // Calculate the complexity metrics for the file
  metrics.push(escomplex.analyse(fileContent));
});

// Aggregate the results
const aggregatedMetrics = metrics.reduce((acc, curr) => {
  acc.aggregate.cyclomatic += curr.aggregate.cyclomatic;
  acc.aggregate.halstead += curr.aggregate.halstead;
  acc.aggregate.sloc += curr.aggregate.sloc;
  acc.methods = [...acc.methods, ...curr.methods];
  acc.functions = [...acc.functions, ...curr.functions];
  return acc;
});

// Print the results
console.log('Aggregated Metrics:', aggregatedMetrics);
