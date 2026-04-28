class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # indices = []
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                # complementIndex = seen[complement]
                # indices.append(complementIndex)
                # indices.append(index)
                return [seen[complement], index]
            
            seen[num] = index