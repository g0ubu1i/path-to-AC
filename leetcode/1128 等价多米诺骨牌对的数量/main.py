class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count_dict = dict()
        for i in dominoes:
            if i[0] > i[1]:
                item = tuple([i[1],i[0]])
            else:
                item = tuple(i)
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1
        count = 0
        for v in count_dict.values():
            if v != 1:
                count += ((v*(v-1))//2)
        return count