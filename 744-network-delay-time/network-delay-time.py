import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adjacency list: store neighbors and weights
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))  # from node u to node v with weight w

        # minHeap stores (time, node)
        minHeap = [(0, k)]
        visited = set()
        time = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)  # get smallest weighted node
            if n1 in visited:
                continue
            visited.add(n1)
            time = max(time, w1)  # update time as max of current and new weight

            # explore neighbors
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        # if we visited all nodes, return total time, else return -1
        return time if len(visited) == n else -1
