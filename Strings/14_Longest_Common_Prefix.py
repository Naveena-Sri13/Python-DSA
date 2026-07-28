class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref=strs[0]
        string=""
        for i in range(len(ref)):
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=ref[i]:
                    return string
            string+=ref[i]
        return string
