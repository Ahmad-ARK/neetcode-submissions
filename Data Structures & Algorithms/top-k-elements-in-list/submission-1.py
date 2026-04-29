class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequency = {}
        for num in nums:
            if num not in numFrequency:
                numFrequency[num] = 1
            else:
                numFrequency[num] += 1

        return sorted(numFrequency, key=lambda x: numFrequency[x], reverse=True)[:k]
        