class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newset:set = set(nums)
        if len(newset) != len (nums):
            return True
        else:
            return False
        