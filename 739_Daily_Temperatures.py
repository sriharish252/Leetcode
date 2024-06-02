from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # Idea: Monotonic Decreasing Stack
    result = [0]*len(temperatures)
    
    # We store all unfound temperatures in the stack, along with it's index
    #   key: index of the element in original temp array, value: temperature value
    stack = []
    for index, temp in enumerate(temperatures):
        # if stack is not empty and current temperature is greater than stack value
        while stack and temp > stack[-1][1]:
            # Remove the top element in stack and assign the number of days in result
            stackIndex, stackTemp = stack.pop()
            result[stackIndex] = index - stackIndex
        # Add the current temperature to stack to find it's result in the next iterations
        stack.append([index, temp])
    return result

# Time Complexity - O(n)
# Space Complexity - O(n)