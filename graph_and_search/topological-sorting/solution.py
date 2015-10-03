# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from Queue import Queue
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        # write your code here
        self.in_degree_count = {}
        for node in graph:
            for neighbor in node.neighbors:
                if neighbor in self.in_degree_count:
                    self.in_degree_count[neighbor] +=1
                else:
                    self.in_degree_count[neighbor] = 1

        result = []
        queue = Queue()
        for node in graph:
            if node not in self.in_degree_count:
                result.append(node)
                queue.put(node)

        while not queue.empty():
            head = queue.get()
            for neighbor in head.neighbors:
                self.in_degree_count[neighbor]-=1
                if self.in_degree_count[neighbor] == 0:
                    result.append(neighbor)
                    queue.put(neighbor)
        return result

