class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
       dis={}
       result=[]
       for num in nums:
        dis[num]=True

       for i in range(1,len(nums)+1):
        if i not in dis:
            result.append(i)
       return result
