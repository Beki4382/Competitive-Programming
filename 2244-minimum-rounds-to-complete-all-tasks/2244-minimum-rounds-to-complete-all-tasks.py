class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count_frequency = Counter(tasks)
        result = 0
        for element in count_frequency:
            if count_frequency[element] == 1:
                return -1
            result += int((count_frequency[element] + 2) / 3)
        return result

        