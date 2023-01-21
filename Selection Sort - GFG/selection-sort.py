#User function Template for python3

class Solution: 
    def select(self, arr, i):
        mini = i
        for k in range(i,len(arr)):
            if arr[mini] > arr[k]:
                mini = k
        
        return mini
        
    def selectionSort(self, arr,n):
        
        for i in range(len(arr)):
            minNum_idx = self.select(arr,i)
            
            arr[i],arr[minNum_idx] = arr[minNum_idx],arr[i]
            
        return arr
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #     min = i
    #     for k in range (len(arr)):
    #         if (arr[k]<=arr[min]):
    #             min = k
    #         if (arr[k]> arr[min]):
    #             continue
            
    #     return min
    
    # def selectionSort(self, arr,n):
    #     for i in range (n):
    #         min = self.select(arr, i)
    #         if (min != i):
    #             arr[min],arr[i] = arr[i], arr[min]
    #         else
    #             arr[i] = arr[min]
                
    #     return arr

            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends