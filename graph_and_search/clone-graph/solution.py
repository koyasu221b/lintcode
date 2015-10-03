# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}

    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return None

        nodes = []
        nodes.append(node)
        self.dict[node] = UndirectedGraphNode(node.label)
        start = 0
        while start < len(nodes):
            head = nodes[start]
            for neighbor in head.neighbors:
                if neighbor not in self.dict:
                    self.dict[neighbor] = UndirectedGraphNode(neighbor.label)
                    nodes.append(neighbor)
            start+=1

        for each_node in nodes:
            clone_node = self.dict[each_node]
            for each_node_neighbor in each_node.neighbors:
                clone_node_neighbor = self.dict[each_node_neighbor]
                clone_node.neighbors.append(clone_node_neighbor)

        return self.dict[node]
