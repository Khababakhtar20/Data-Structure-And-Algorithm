class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for u,v in edges:
            if u not in graph:
                graph[u]= []
            if v not in graph:

                graph[v]= []
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def find_path(node,visited):
            if node == destination:
                return True
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if find_path(neighbor,visited):
                        return True
            return False

        return find_path(source,visited)


            
            
        