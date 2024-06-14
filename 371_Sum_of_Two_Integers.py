def getSum(a: int, b: int) -> int:
    # Since Python's integers are arbitrarily long (>32 bits), we need to constrain it to 32 bits.
    # Using a 32-bit mask to handle overflow and -ve numbers, ignore anything over 32 bits
    #   0xffffffff is hexadecimal which is equal to 32 1s in binary
    mask = 0xffffffff
    while (b & mask) > 0:
        carry = ( a & b ) << 1
        a = (a ^ b) 
        b = carry
    # to handle overflow
    return (a & mask) if b > 0 else a

# Time - O(1) => Since the constraints are low, this is linear time.
# Space - O(1)

'''
// JAVA Solution:
public int getSum(int a, int b) {
    while(b != 0) {
        int carry = (a&b)<<1;
        // a XOR b
        a = a^b;
        b = carry;
    }
    return a;
}
'''