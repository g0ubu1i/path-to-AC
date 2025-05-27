class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        if length == 1:
            return 1
        temp = 1
        for i in range(length):
            fore_str = s[i]
            count = 1
            for j in range(i+1,length):
                if s[j]  not in fore_str:
                    fore_str += s[j]
                    count += 1
                else:
                    break
            if temp >= count:
                continue
            else:
                temp = count
                continue
        return temp

sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))