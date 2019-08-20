class Solution:
    # 最长公共前缀满足在每个字符串中的开头都是一样的，那么就以一个字符串作为pattern标准来进行匹配，如果后面的字符串和第一个字符串的pattern一样就把它计入最长公共前缀中
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''
        if strs == []:
            return lcp
        for i in range(len(strs[0])):
            pattern = strs[0][i]
            for j in range(1,len(strs)):
                if i >= len(strs[j]):
                    return lcp
                if strs[j][i] != pattern:
                    return lcp
            lcp += pattern
        return lcp
