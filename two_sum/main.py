class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            needed_num = target - nums[i]
            if needed_num in nums and nums.index(needed_num)!=i:
                return [i, nums.index(needed_num)]