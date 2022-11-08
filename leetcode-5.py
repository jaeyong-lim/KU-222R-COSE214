# Leetcode assignment #5
# 1971. Find if Path Exists in Graph
# Submitted 9 Nov 2022

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True
        
        class Node:
            def __init__(self) -> None:
                self.neighbors = set()
                self.visited = False

        nodes = [Node() for i in range(n)]

        for edge in edges:
            nodes[edge[0]].neighbors.add(edge[1])
            nodes[edge[1]].neighbors.add(edge[0])

        queue = [nodes[source]]
        for u in queue:
            for v in u.neighbors:
                if v == destination:
                    return True
                if nodes[v].visited == False:
                    nodes[v].visited = True
                    queue.append(nodes[v])

        return False
