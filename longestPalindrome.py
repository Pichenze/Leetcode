class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s 

        longest_len = 1  #最长回文串的长度
        res = s[0]  #初始化最长回文串
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]  #初始化 状态量 dp[l][r]表示s字符串s[l:r+1]是否是回文串的布尔值
        for l in range(len(s)-1):
            for r in range(l+1,len(s)):
                if s[l] == s[r] and (l+1 <= r-1 or dp[l+1][r-1]):  # 当且仅当s[l]==s[r]并且 s[l-1:(r-1)+1]是回文串，或是l,r之间最多只有一个字符（一个字符也可以称为回文串），s[l:r+1才是回文串]
                    dp[l][r] = True
                    if r-l+1 > longest_len:
                        longest_len = r-l+1
                        res = s[l:r+1]
        return res
