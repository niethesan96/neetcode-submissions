
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=sorted([i.start for i in intervals])
        end=sorted([i.end for i in intervals])
        start_ptr=0
        end_ptr=0
        rooms=0
        while start_ptr<len(intervals):
            if start[start_ptr]<end[end_ptr]:
                rooms+=1
            else:
                end_ptr+=1
            start_ptr+=1
        return rooms