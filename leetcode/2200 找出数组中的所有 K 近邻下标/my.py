class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        index = []
        for i in range(len(nums)):
            if nums[i]==key:
                index = list(set(index)|set([i for i in range(i-k,i+k+1)]))
        return list(set(index)&set([i for i in range(len(nums))]))
    
sol = Solution()
result = sol.findKDistantIndices(nums=[2,1,1,1,2],key=2,k=1)
print(result)

