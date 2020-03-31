# Accounts Merge
class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """

    def accountsMerge(self, accounts):
        # write your code here
        if not accounts:
            return []
        graph, users, parents, result = {}, {}, {}, []
        for account in accounts:
            if not account or len(account) < 2:
                continue
            user, start_node = account[0], account[1]
            if start_node not in graph:
                graph[start_node] = start_node
                users[start_node] = user
            length = len(account)
            if length == 2:
                continue
            for node in account[2:]:
                if node not in graph:
                    graph[node] = node
                    users[node] = user
                self.union(start_node, node, graph)

        for child in graph:
            parent = self.find(child, graph)
            if parent not in parents:
                parents[parent] = [child]
            else:
                parents[parent].append(child)
        for parent, childs in parents.items():
            result.append([users[parent]] + sorted(childs))
        return result

    def union(self, node_x, node_y, graph):
        x_parent = self.find(node_x, graph)
        y_parent = self.find(node_y, graph)
        if x_parent != y_parent:
            graph[x_parent] = y_parent

    def find(self, node, graph):
        child_nodes = []
        while graph[node] != node:
            child_nodes.append(node)
            node = graph[node]
        for child in child_nodes:
            graph[child] = node
        return node

