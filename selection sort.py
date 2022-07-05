
class Solution: 
    def select(self, arr, i):
        min = i
        for k in range(i, len(arr)):
            if(arr[k] <= arr[min]):
                min = k
        return min
    
    def selectionSort(self, arr,n):
        for i in range (n):
            min = self.select(arr, i)
            arr[i], arr[min] = arr[min], arr[i]
        return arr
