class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_map = { i : [] for i in range(numCourses)}
        for pre,course in prerequisites:
            prerequisites_map[pre].append(course)
        # the above creates a hashmap of all the courses and their pre in a list 
        visted_set = set()
        def dfs(course):
            if course in visted_set:
                return False
            if prerequisites_map[course] == []:
                return True

            visted_set.add(course)
            for crs in prerequisites_map[course]:
                if not dfs(crs):return False #if one of them returns false then return false on the function#loop ensure u visted all the possible courses for that course  
            visted_set.remove(course)# since vist done remove from hash other vist my tripup without having cycle
            prerequisites_map[course] = [] # set og set to 0
            return True
        # u need to loop dfs through all course since there is a change there are two disconnencted graphs
        for i in range(numCourses):
            if not dfs(i):return False
        return True

        # if not dfs(crs):return False interesting way to ensure one false triggers false on the whole if all true we have a true 