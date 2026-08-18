class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in mapping:
                return [mapping[diff], i]
            mapping[val] = i
        return [-1,-1]