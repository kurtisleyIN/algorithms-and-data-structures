# python3
import sys
import random
from copy import deepcopy

def eulerian_cycle(adj_dict):
    
    # Dictionary that tracks remaining edges (those not yet taken),
    # initialized as the input adjacency dict
    remain_d = deepcopy(adj_dict)
    
    # Randomly select a starting node
    node = random.choice(list(adj_dict.keys()))
    
    # Create list to track Eulerian cycle
    cycle = [node] 

    # Continue as long as there are edges that remain untaken    
    while remain_d:

        # Check if any adjacencies remain for the node and if so, how many        
        value = remain_d.get(node)
        
        # If the node has no unused edges, we must be back at V0 (since the 
        # graph is balanced), but we also know there are remaining edges out 
        # there. We need to expand the circle until it encompasses all nodes.
        if value == None:
                       
            # To do so, iterate through the current "cycle" until we find a 
            # node with an unused edge. Make that the new V0.
            for i, n in enumerate(cycle):
                if remain_d.get(n):
                    node = n
                    cycle = cycle[i:]+cycle[1:i+1]
                    break
                
        # If the node has a single unused edge, simply use it to continue the 
        # cycle by adding it to the list 'cycle' and removing it from the dict
        elif len(value) == 1:       
            node = remain_d.pop(node)[0]
            cycle.append(node)
            
        # If the node has multiple unused edges, randomly select one to add to 
        # the cycle and remove it out from the node's list of adjacencies.
        elif len(value) > 1:
            if node in value:
                random_i = value.index(node)
            else:
                random_i = random.randrange(len(value))
            pos_nodes = remain_d[node]
            new_node = pos_nodes.pop(random_i) 
            remain_d[node] = pos_nodes
            node = new_node
            cycle.append(node)

    return cycle

if __name__ == "__main__":
    input = sys.stdin.read().strip().splitlines()
    edges = [tuple(edge.split(' -> ')) for edge in input if edge]
    edges = [(int(t[0]), [int(i) for i in t[1].split(',')]) for t in edges]
    graph = {x: y for x, y in edges}
    cycles = eulerian_cycle(graph)
    print ('->'.join([str(i) for i in cycles]))


