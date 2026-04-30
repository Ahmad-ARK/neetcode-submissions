class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # length = len(nums)
        # newArray = []
        # for i in range(0, length):
        #     currentNum = nums[i]
        #     j = 0
        #     thisProduct = 1
        #     while j < length:
        #         if j == i:
        #             j += 1
        #         else:
        #             thisProduct *= nums[j]
        #             j += 1
        #     newArray.append(thisProduct)
        # return newArray


        # length = len(nums)
        # prefix = [1] * length
        # suffix = [1] * length
        # output = [1] * length

        # for i in range(1, length):
        #     prefix[i] = prefix[i-1] * nums[i-1]

        # for i in range(length-2, -1, -1):
        #     suffix[i] = suffix[i+1] * nums[i+1]

        # for i in range(length):
        #     output[i] = prefix[i] * suffix[i]
        # return output 

        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        output = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            output[i] = prefix[i] * suffix[i]
        
        return output
