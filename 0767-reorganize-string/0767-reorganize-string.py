class Solution:
    def reorganizeString(self, s: str) -> str:
        character_count = {}
        for char in s:
            character_count[char] = character_count.get(char, 0) + 1

        most_frequent_char = None
        most_frequent_count = None

        for char, count in character_count.items():
            if most_frequent_count is None or count > most_frequent_count:
                most_frequent_count = count
                most_frequent_char = char

        if most_frequent_count > ((len(s) + 1) // 2):
            return ""

        result = (len(s)) * ['']
        index = 0

        while most_frequent_count:
            result[index] = most_frequent_char
            index += 2
            most_frequent_count -= 1

        for char, count in character_count.items():
            if char not in result:
                remaining_count = count
                while count:
                    if index >= len(s):
                        index = 1
                    result[index] = char
                    index += 2
                    count -= 1

        return "".join(result)
