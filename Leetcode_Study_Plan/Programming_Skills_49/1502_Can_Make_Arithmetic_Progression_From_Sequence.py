class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr=sorted(arr)
        
        q=arr[1]-arr[0]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]!=q:
                return False
        return True
    
