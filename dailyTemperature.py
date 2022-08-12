class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer =[0]*len(temperatures)
        stack =[]
        for i, t in enumerate(temperatures):
            while stack and t >stack[-1][1]:
                stackInd , stackT = stack.pop()
                answer[stackInd] = (i-stackInd)
            stack.append([i,t])
        return answer
