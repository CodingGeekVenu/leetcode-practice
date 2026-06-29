class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0 

        max_diff = 0

        nums = sorted(nums)

        for i in range(len(nums) - 1):
            if (nums[i + 1] - nums[i] > max_diff):
                max_diff = nums[i + 1] - nums[i]
        
        return max_diff