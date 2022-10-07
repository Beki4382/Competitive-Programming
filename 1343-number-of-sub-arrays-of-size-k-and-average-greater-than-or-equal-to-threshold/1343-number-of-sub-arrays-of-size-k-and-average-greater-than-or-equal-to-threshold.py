class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        l, r = 0,k
        count = 0
        total = sum(arr[:k])
        if total/k >= float(threshold):
            count +=1

        for i in range(len(arr) - k):
            total += (-1) * arr[i] + arr[i + k]  
            if total / k >= float(threshold):
                count += 1
        return count


