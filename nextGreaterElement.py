class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        dic = {}
        ans = []
        for i in nums2:
            if len(stack)==0:
                stack.append(i)
            else:
                while(stack and i>stack[-1]):
                    dic[stack.pop()]= i
                stack.append(i)
        for j in stack:
            dic[j] = -1
        return [dic[key] for key in nums1]
                
                    
