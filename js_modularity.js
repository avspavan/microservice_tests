const { Graph } = require('graphology');
const louvain = require('graphology-communities-louvain');

function calculateModularity(serviceDependencies) {
  // Convert the service's module dependencies to a graph
  const graph = new Graph();
  for (const [module, dependencies] of Object.entries(serviceDependencies)) {
    graph.mergeNode(module);
    for (const dependency of dependencies) {
      graph.mergeNode(dependency);
      graph.addEdge(module, dependency);
    }
  }

  // Compute the modularity of the service using the Louvain algorithm
  const { communities } = louvain(graph);

  const modularity = graph.modularity(communities);
  console.log(`The modularity of the service is ${modularity}`);
}

// Example service module dependencies
const serviceDependencies = {
  module1: ['module2'],
  module2: ['module3'],
  module3: ['module4'],
  module4: [],
};

calculateModularity(serviceDependencies);
