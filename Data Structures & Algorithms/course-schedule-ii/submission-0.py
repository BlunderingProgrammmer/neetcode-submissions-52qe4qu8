from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #intialize the adj list , indegree array and the q
        adj_list = [ [] for _ in range(numCourses)] # list at each index since course from 0 - n-1 where n is numCourses
        indegree_array = [0] * numCourses
        q = deque()
        output = []

        for crs,pre in prerequisites:
            adj_list[pre].append(crs) #for crs index append prerequisites
            indegree_array[crs] += 1 # each time the same course comes up add 1 in the indegree_array

        #initialization done here
        #intialize the que
        for i in range(len(indegree_array)):
            if indegree_array[i] == 0:
                q.append(i) # append i cuz i is the crs number that is ready for precossing

        #bfs traversal_here
        while q:
            node = q.popleft()
            output.append(node)
            #process node using adj list
            for neigbhors in adj_list[node]:
                indegree_array[neigbhors] -=1
                if indegree_array[neigbhors] == 0:
                    q.append(neigbhors)
        return output if len(output) == numCourses else []