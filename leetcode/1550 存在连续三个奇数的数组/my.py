class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        length = len(arr)
        for i in range(length-2):
            print(arr[i])
            if arr[i] % 2 == 1 and arr[i+1] % 2 ==1 and arr[i+2]%2 == 1:
                return True
            else:
                pass
        return False

sol = Solution()
print(sol.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))