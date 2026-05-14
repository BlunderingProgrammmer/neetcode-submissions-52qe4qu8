from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for crs, pre in prerequisites:
            adj[pre].append(crs)  # Flow: Prereq comes FIRST
            indegree[crs] += 1    # This course is WAITING on a prereq
            
        # 2. Find starting points (Indegree == 0)
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        output = []
        # 3. BFS Process
        while q:
            node = q.popleft()
            output.append(node)
            
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    
        # 4. Final Cycle Check
        return  len(output) == numCourses 