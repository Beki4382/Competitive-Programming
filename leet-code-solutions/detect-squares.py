class DetectSquares:

    def __init__(self):
        self.pointsDict = defaultdict(int)
        self.pointsList = []

    def add(self, point: List[int]) -> None:
        self.pointsDict[tuple(point)] += 1
        self.pointsList.append(point)

    def count(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]
        ans = 0
        for px, py in self.pointsList:
            if (abs(x - px) != abs(y - py)) or x == px or y == py:
                continue
            ans += self.pointsDict[(x,py)] * self.pointsDict[(px, y)]
        return ans 

       
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)