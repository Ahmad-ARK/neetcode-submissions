class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        newArray = []
        for i in range(0, length):
            currentNum = nums[i]
            j = 0
            thisProduct = 1
            while j < length:
                if j == i:
                    j += 1
                else:
                    thisProduct *= nums[j]
                    j += 1
            newArray.append(thisProduct)
        return newArray




            
        