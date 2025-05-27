class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        possible = []
        for i in range(1,7):
            count = 0
            for j in range(len(tops)):
                if tops[j-1] == i or bottoms[j-1] == i:
                    count += 1
            if count == len(tops):
                possible.append(i)
        possible_result=[]
        if possible:
            for i in possible:
                count_1 = 0
                count_2 = 0
                for j in range(len(tops)):
                    if tops[j] == i and bottoms[j] == i:
                        pass
                    elif tops[j] == i and bottoms[j] != i:
                        count_1 += 1
                    elif bottoms[j] == i and tops[j] != i:
                        count_2 += 1
                possible_result.append(min(count_1,count_2))
            return min(possible_result)
        else:
            return -1
        
sol = Solution()
print(sol.minDominoRotations(tops = [1,1,1,1,1,1,1], bottoms = [1,1,1,1,1,1,1]))