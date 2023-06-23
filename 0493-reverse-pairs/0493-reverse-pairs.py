class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        if len(nums) > 1:
            mid = len(nums)//2
            leftHalf = nums[:mid]
            rightHalf = nums[mid:]
            count += self.reversePairs(leftHalf)
            count += self.reversePairs(rightHalf)

            i = j = 0
            for i in range(len(leftHalf)):
                while j < len(rightHalf) and leftHalf[i] > (2 * rightHalf[j]):
                    j += 1
                count += j

            i = j = k = 0

            while i < len(leftHalf) and j < len(rightHalf):
                if leftHalf[i] > rightHalf[j]:
                    nums[k] = rightHalf[j]
                    j += 1
                    k += 1

                else:
                    nums[k] = leftHalf[i]
                    i += 1
                    k += 1

            while j < len(rightHalf):
                nums[k] = rightHalf[j]
                j += 1
                k += 1

            while i < len(leftHalf):
                nums[k] = leftHalf[i]
                i += 1
                k += 1

        return count
    
