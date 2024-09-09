class Solution:
    def uniqueOccurrences(self, arr):
        count_map = {}
        
        for num in arr:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        count_set = set(count_map.values())
        
        return len(count_set) == len(count_map)