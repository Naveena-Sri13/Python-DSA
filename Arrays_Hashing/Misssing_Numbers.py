class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        miss={}
        result=[]
        num=0

        for i in range(0,len(nums)+1):
            if i in nums:
                result.append(i)
            else:
                num+=i
        return num
