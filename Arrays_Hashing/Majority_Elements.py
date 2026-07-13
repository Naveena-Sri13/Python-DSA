class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj={}
        
        for num in nums:
            if num in maj:
                maj[num]+=1
            else:
                maj[num]=1
            if maj[num] > len(nums)//2:
                return num
