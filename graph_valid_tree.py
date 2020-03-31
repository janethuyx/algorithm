class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if n == 0:
            return False
        if n - 1 != len(edges):
            return False
        graph = {}
        for node in range(n):
            graph[node] = node
        for index in range(len(edges)):
            node_x, node_y = edges[index][0], edges[index][1]
            parent_x, parent_y = self.find_parent(node_x, graph), self.find_parent(node_y, graph)
            if parent_x == parent_y:
                return False
            graph[parent_x] = parent_y
        return True

    def find_parent(self, node, graph):
        child_nodes = []
        while graph[node] != node:
            child_nodes.append(node)
            node = graph[node]
        for child in child_nodes:
            graph[child] = node
        return node

