class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [0] * n
        available = [i for i in range(n)]
        occupiedrooms = []
        heapify(occupiedrooms)
        heapify(available)

        sortedMeetings = sorted(meetings, key = lambda x: x[0])
        for start, end in sortedMeetings:
            while occupiedrooms and occupiedrooms[0][0] <= start:
                en, room = heappop(occupiedrooms)
                heappush(available, room)
            if available:
                room = heappop(available)
                heappush(occupiedrooms, [end, room])
            else:
                currEnd, room = heappop(occupiedrooms)
                newEnd = currEnd + (end - start)
                heappush(occupiedrooms, [newEnd,room])
            rooms[room] += 1
                
        maxOccupied = max(rooms)
        res = rooms.index(maxOccupied)
        return res
        