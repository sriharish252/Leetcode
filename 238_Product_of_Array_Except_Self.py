from typing import List

def productExceptSelf(self, nums: List[int]) -> List[int]:
    # IDEA: prefixProduct*suffixProduct = product of array except self
    #       Make sure the prefix and suffix doesn't include the current index variable
    length = len(nums)
    result = [1]*length

    prefixProd = 1
    # Calculate the prefixProduct and store in result array
    for i in range(length):
        result[i] = prefixProd
        prefixProd *= nums[i]
    
    suffixProd = 1
    # Calculate the suffix product and update the result
    for i in range(length-1, -1, -1):
        # result = (prefixProd stored in result[])*suffixProd
        result[i] *= suffixProd
        suffixProd *= nums[i]
    
    return result

# Time Complexity - O(n)
# Space Complexity - O(1)