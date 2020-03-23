"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                visited.add(v)
                print(v) 
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v) 
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)  # TODO

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        def recurse(stack, visited):
            v = stack.pop()
            if v not in visited:
                print(v)
                visited.add(v)

                for next_vertex in self.vertices[v]:
                    stack.push(next_vertex)
            if stack.size():
                recurse(stack, visited)
        
        recurse(stack, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
    
        while q.size():
            p = q.dequeue()
            v = p[len(p)-1]
            if v not in visited:
                if v == destination_vertex:
                    return p
            
                visited.add(v)
                
                for next_vertex in self.vertices[v]:
                    p_copy = p[:]
                    p_copy.append(next_vertex)
                    q.enqueue(p_copy)
        
        return False 

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()
    
        while s.size():
            p = s.pop()
            v = p[len(p) - 1]
            
            if v not in visited:
                if v == destination_vertex:
                    return p
                visited.add(v)
                
                for next_vertex in self.vertices[v]:
                    p_copy = p[:]
                    p_copy.append(next_vertex)
                    s.push(p_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        correct_path = []
        def recurse(stack, visited):
            p = stack.pop()
            v = p[len(p) - 1]
            
            if v not in visited:
                if v == destination_vertex:
                    nonlocal correct_path
                    correct_path = p
                    return 
                
                visited.add(v)

                for next_vertex in self.vertices[v]:
                    p_copy = p[:]
                    p_copy.append(next_vertex)
                    stack.push(p_copy)
            if stack.size():
                recurse(stack, visited)
            
        
        recurse(stack, visited)
        return correct_path  # TODO
        

