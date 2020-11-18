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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex doesn't exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #make a queue
        q = Queue()

        # make a set to track which nodes we have visited
        visited = set()

        #enqueue the starting node
        q.enqueue(starting_vertex)

        #loop while the queue isn't empty
        
        while q.size() > 0:
            #take the current node out of the queue
            current_node = q.dequeue()

            #check if it has been visited, if not add it to visited
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                #get the current node's neighbors and add them to the queue (this is how you traverse)
                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    q.enqueue(neighbor)


            

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()

        visited = set()

        s.push(starting_vertex)

        while s.size() > 0:
            current_node = s.pop()

            if current_node not in visited:
                print(current_node)
                visited.add(current_node)

                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    s.push(neighbor)
        




    def dft_recursive(self, vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if vertex not in visited:
            print(vertex)
            visited.add(vertex)

            neighbors = self.get_neighbors(vertex)
            if len(neighbors) == 0:
                return
            
            else:
                for neighbor in neighbors:
                    self.dft_recursive(neighbor, visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #SEARCH

        q = Queue()
        visited = set()
        #enqueue PATH to starting vertex
        q.enqueue([starting_vertex])

        while q.size() > 0:
            #dequeue, this is our current path
            current_path = q.dequeue()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path

            #check if it has been visited, if not add it to visited
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                #get the current node's neighbors and add them to the queue (this is how you traverse)
                neighbors = self.get_neighbors(current_node)

                #iterate over the neighbors, enqueue the PATH to them
                for neighbor in neighbors:
                    path_copy = list(current_path)
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #SEARCH
        s= Stack()
        visited = set()

        s.push([starting_vertex])

        while s.size() > 0:
            current_path = s.pop()
            current_node = current_path[-1]

            if current_node not in visited:
                if current_node == destination_vertex:
                    return current_path

                visited.add(current_node)

                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    path_copy = list(current_path)
                    path_copy.append(neighbor)
                    s.push(path_copy)
                    
    #search just brings the path along with the current_node 

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
