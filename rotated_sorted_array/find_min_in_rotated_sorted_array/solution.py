class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        start, end = 0, len(num) -1
        compare = num[end]
        while start + 1 < end:
            mid = start + (end - start)/2
            if num[mid] > compare:
                start = mid
            elif num[mid] == compare:
                end = mid
            elif num[mid] < compare:
                end = mid

        if num[start] < num[end]:
            return num[start]

        return num[end]

