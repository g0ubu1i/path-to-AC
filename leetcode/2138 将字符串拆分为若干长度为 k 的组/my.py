class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        result = []
        for i in range(0,len(s),k):
            if (i + k) > len(s):
                result.append(s[i:len(s)]+fill*(i+k-len(s)))
            else:
                result.append(s[i:i+k])
        return result

solu = Solution()
print(solu.divideString("abcdefghi",k=3,fill="x"))