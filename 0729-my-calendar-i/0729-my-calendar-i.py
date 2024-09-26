import sortedcontainers
class MyCalendar(object):

    def __init__(self):
        self.calendar = sortedcontainers.SortedList()

    def book(self, start, end):
        if not self.calendar:
            self.calendar.add((start, end))
            return True
        
        prev_index = self.calendar.bisect_left((start, end)) - 1
        next_index = self.calendar.bisect_right((start, end))

        if (start, end) in self.calendar:
            return False
        
        if (prev_index == -1 or self.calendar[prev_index][1] <= start) and (next_index == len(self.calendar) or self.calendar[next_index][0] >= end):
            self.calendar.add((start, end))
            return True
        
        return False
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)