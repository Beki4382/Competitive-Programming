class Solution(object):
    def distanceFinder(self, points, i):
            return math.sqrt(points[i][0]**2 + points[i][1]**2)
            
    def kClosest(self, points, k):
        for i in range(len(points)):
            min = i
            j = i+1
            distance = self.distanceFinder(points, i)
            points[i].append(distance)
            for j in range(len(points)):
                if(points[j][-1] < points[min][-1]):
                    min = j
                points[j], points[min] = points[min], points[j]
        return [points[i][:-1] for i in range(k) ]
       
