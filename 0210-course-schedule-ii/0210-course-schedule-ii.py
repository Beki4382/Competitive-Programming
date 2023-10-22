class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj_list[course].append(pre)
        
        visited = [0] * numCourses
        course_order = []  # Store the course order

        def dfs(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            visited[course] = -1
            
            for pre in adj_list[course]:
                if not dfs(pre):
                    return False
            
            visited[course] = 1
            course_order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
       
        return course_order
