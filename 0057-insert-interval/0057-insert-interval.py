class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        mergedArray = [intervals[0]]
        for i in range(1,len(intervals)):
            if mergedArray[-1][1] >= intervals[i][0]:
                mergedArray[-1] = [min(mergedArray[-1][0], intervals[i][0]),max(mergedArray[-1][1], intervals[i][1])]
            else:
                mergedArray.append(intervals[i])
        return mergedArray
            
                
        
        