class Solution:
    def max_of_subarrays(self,arr,n,k):
        
        if not arr or k == 0:
            return []
        
        maximums = []
        
        max_score = max(arr[:k])
        maximums.append(max_score)
        left = 0
        
        for i in range(k,len(arr)):
            
            if arr[left] == max_score:
                max_score = max(arr[left+1:i+1])
            else:
                max_score = max(max_score, arr[i])
            
            left += 1    
            maximums.append(max_score)
        
        
        return maximums