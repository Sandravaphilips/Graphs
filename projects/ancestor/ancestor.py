from util import Stack
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    new_graph = Graph()
    s = Stack()
    s.push([starting_node])
    visited = set()
    path = []

    for i in ancestors:
        for j in i:
            if j not in visited:
                new_graph.add_vertex(j)
                visited.add(j)
    
    for i in ancestors:
        new_graph.add_edge(i[1], i[0])
    visited = set()
    while s.size():
        p = s.pop()
        v = p[len(p) - 1]
        
        if v not in visited:
            if len(new_graph.vertices[v]) == 0:
                path.append(p)
            visited.add(v)
            
            for next_vertex in new_graph.vertices[v]:
                p_copy = p[:]
                p_copy.append(next_vertex)
                s.push(p_copy)
    
    longest_path = path[0]
    for v in path:
        if len(v) > len(longest_path):
            longest_path = v
        if (len(v) == len(longest_path)) and (v[-1] < longest_path[-1]):
            longest_path = v
    
    result = longest_path[-1]
    if result == starting_node:
        return -1
    else:
        return result