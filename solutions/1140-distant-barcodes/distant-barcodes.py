# In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].
#
# Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.
#
#  
#
# Example 1:
#
#
# Input: [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
#
#
#
# Example 2:
#
#
# Input: [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,2,1,2,1]
#
#
#  
#
# Note:
#
#
# 	1 <= barcodes.length <= 10000
# 	1 <= barcodes[i] <= 10000
#
#
#
#  
#


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        i, n = 0, len(barcodes)
        res = [0] * n
        
        for barcode,count in Counter(barcodes).most_common():
            for _ in range(count):
                res[i] = barcode
                i += 2
                if i > n - 1:
                    i = 1
                    
        return res
        
