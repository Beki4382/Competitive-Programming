
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
