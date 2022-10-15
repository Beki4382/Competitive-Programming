class Solution(object):
    def distanceFinder(self, points, i):
            return math.sqrt(points[i][0]**2 + points[i][1]**2)
            
    def kClosest(self, points, k):
        for i in range(len(points)):
            distance = self.distanceFinder(points, i)
            points[i].append(distance)
        points.sort(key= lambda x:x[-1])
        print(points)
            
        return [points[i][:-1] for i in range(k) ]
       
                
        
            
       
        