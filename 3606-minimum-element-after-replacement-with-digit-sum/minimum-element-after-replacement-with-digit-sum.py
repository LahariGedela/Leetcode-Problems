class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def d(x):
            s=0
            while(x>0):
                s+=x%10
                x//=10
            return s
        return min(d(x) for x in nums)