
def numDecodings(s: str) -> int:
    # d1 is max number of decodings for the position 1 index to the right in the string
    # d2 is 2 indices to the right
    # Initially we start from the last digit, so 1 index to the right is end of string
    #   Base Case: Number of Decodings for the End of String is 1 (since there is atleast 1 way to reach there)
    d1, d2 = 1, 0
    currentNumOfDecodings = 0
    # Iterate from end of string to beginning
    for currentIndex in range(len(s)-1, -1, -1):
        currentNumOfDecodings = 0
        
        # If current digit is not 0, add the next index's decodings
        if s[currentIndex] != "0":
            currentNumOfDecodings += d1
        
            # If next digit is not end of string and including it, the string is within 10 to 26, add the two indices' decodings
            if (currentIndex+1 < len(s)) and (s[currentIndex]=="1" or (s[currentIndex]=="2" and s[currentIndex+1] in "0123456")):
                currentNumOfDecodings += d2
        
        # As the currentIndex moves to the beginning, move d1 and d2 1 position left each. So d2 takes d1 position and d1 takes currentIndex position
        d2 = d1
        d1 = currentNumOfDecodings
    
    # Return max number of decodings at current index
    return currentNumOfDecodings

print(numDecodings("112"))

# Time Complexity - O(n)
# Space Complexity - O(1)