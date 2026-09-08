class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        l=len(nums)
        nums.sort()
        s=0
        for i in range(0,l,2):
            s+=nums[i]
        return s
            