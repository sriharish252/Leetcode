from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # Iterative solution: Use a nodeDict to store the newly created clones
        if not node:
            return None
        nodeDict = {}
        stack = [node]
        while stack:
            currentNode = stack.pop()
            # Create new clone if not created already
            if currentNode.val not in nodeDict:
                newNode = Node(currentNode.val, [])
                nodeDict[newNode.val] = newNode
            
            for n in currentNode.neighbors:
                # Create neighbor node clones if not created already and add to stack,
                #   so that their neighbors list can be updated
                if n.val not in nodeDict:
                    stack.append(n)
                    nodeDict[n.val] = Node(n.val, [])
                nodeDict[currentNode.val].neighbors.append(nodeDict[n.val])
        return nodeDict[node.val]

# Time Complexity - O(n)
# Space Complexity - O(n)