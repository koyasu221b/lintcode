class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers = sorted(numbers)
        n = len(numbers)
        import sys
        closet_sum = sys.maxint
        result = []
        for index, number in enumerate(numbers):
            left = index+1
            right = n-1
            while left < right:
                sum = number + numbers[left] + numbers[right]
                closet_sum = sum if abs(target-sum) < abs(target-closet_sum) else closet_sum
                if sum > target:
                    right-=1
                elif sum < target:
                    left+=1
                else:
                    return sum

        return closet_sum
