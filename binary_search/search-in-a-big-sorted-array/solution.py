"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # if there is no number on that index, return -1
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        # write your code here
        start = 0
        end = 0
        result = reader.get(end)
        while result!=-1 and result < target:
            end = end*2 + 1
            result = reader.get(end)

        while start + 1 < end:
            mid = start + (end - start)/2
            result = reader.get(mid)
            if result == target:
                end = mid
            elif result < target:
                start = mid
            else:
                end = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
