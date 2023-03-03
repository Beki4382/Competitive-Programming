class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        count_arr = [0] * 1001 # create array length of trips
        
        for trip in trips:
            if trip[0] > capacity:
                return False 
            count_arr[ trip[1] ] += trip[0] 
            count_arr[ trip[2] ] -= trip[0]
            
        for i in range( 1, len(count_arr) ):
            count_arr[i] += count_arr[i - 1]
            
            if count_arr[i] > capacity:
                return False
        return True
        
       