class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        len_rooms = len(rooms)
        queue = deque([0])
        visited = set()
        
        while queue:
            room = queue.popleft()
            visited.add(room)
        
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
                    
        
        return len_rooms == len(visited)     