class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        friend_pairs = {}
        for x, y in pairs:
            friend_pairs[x] = y
            friend_pairs[y] = x

        unhappy_count = 0
        for x in friend_pairs.keys():
            y = friend_pairs[x]
            index_y = preferences[x].index(y)
            better_friends = preferences[x][:index_y]

            for u in better_friends:
                v = friend_pairs[u]
                index_v = preferences[u].index(v)

                if x in preferences[u][:index_v]:
                    unhappy_count += 1
                    break

        return unhappy_count

        