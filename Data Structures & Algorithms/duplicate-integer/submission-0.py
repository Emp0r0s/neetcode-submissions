class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newset:set = set()
        for i in nums:
            if i not in newset:
                newset.add(i)
            else:
                return True
        return False
        