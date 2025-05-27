class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        fore_key = ""
        fore_index = 0 
        length = len(dominoes)
        result = ["."]*length
        for i in range(length):
            if dominoes[i] == "L":
                if fore_key == "" or fore_key == "L":
                    result[fore_index:i+1] = "L"*(i+1)
                    fore_key = dominoes[i]
                    fore_index = i
                elif fore_key == "R":
                    if (i-fore_index+1) % 2 == 1:
                        result[(i+fore_index) // 2] = "."
                        result[fore_index:(i+fore_index)//2] = "R"*((i+fore_index)//2 - fore_index)
                        result[(i+fore_index)//2+1:i+1] = "L"* ((i+fore_index)//2 - fore_index)
                        fore_index =i
                        fore_key = "L"
                    else:
                        result[fore_index:((i+fore_index)//2) +1] = "R"*((i-fore_index+1)//2)
                        result[((i+fore_index)//2)+1:i+1] = "L"*((i-fore_index+1)//2)
                        fore_index = i
                        fore_key = "L"
            elif dominoes[i] == "R":
                if fore_key == "R":
                    result[fore_index:i+1] = "R"*(i-fore_index+1)
                if "L" not in dominoes[i+1:length+1] and "R" not in dominoes[i+1:length+1]:
                    result[i:length+1] = "R"*(length-i)
                fore_index = i
                fore_key = "R"
            print(result)
        re = "".join(result)
        return re

sol = Solution()
print(sol.pushDominoes(dominoes = "L.....RR.RL.....L.R."))