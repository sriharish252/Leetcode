from typing import List

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Stores the prerequisite list for each course
    prereqMap = {i:[] for i in range(numCourses)}
    for course, prereq in prerequisites:
        prereqMap[course].append(prereq)
    
    visitedSet = set()
    
    def dfs(course):
        # If the course is already visited, there is a loop, so False
        if course in visitedSet:
            return False
        # If there are no prerequisites, then this course can be taken, return True
        if len(prereqMap[course]) <= 0:
            return True
        
        # Add the current course to the visited set and proceed dfs-ing into it's prerequisites
        visitedSet.add(course)
        for prereq in prereqMap[course]:
            if not dfs(prereq):
                return False
        visitedSet.remove(course)
        prereqMap[course] = []
        return True
    
    for course in range(numCourses):
        if not dfs(course):
            return False
    return True

# Time Complexity - O(n+p) => n:number of courses, p:length of prerequisites list
# Space Complexity - O(n+p)