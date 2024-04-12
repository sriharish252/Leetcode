from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        matrix = []
        count = [0]*(len(nums)+1)
        for number in nums:
            # Update count value
            count[number] += 1

            # Max Count value determines number of rows in matrix, 
            #   so add new matrix row if (length of matrix) is less than any count value
            if len(matrix) < count[number]:
                matrix.append([])
            
            # Add the number to the matrix row
            #   If a number has two counts, it'll be added to the 1st and 2nd row of matrix
            #   when corresponding count value is incremented
            matrix[count[number] - 1].append(number)    # -1 because index starts from 0
        return matrix

# Time - O(n)
# Space - O(n)