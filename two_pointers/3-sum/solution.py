class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        result = []
        numbers = sorted(numbers)
        n = len(numbers)
        for index in range(n):
            if index > 0 and numbers[index] == numbers[index-1]:
                continue
            start = index+1
            end = n-1
            while start < end:
                if start > index+1 and numbers[start] == numbers[start-1]:
                    start+=1
                    continue
                sum = numbers[index] + numbers[start] + numbers[end]
                if sum == 0:
                    tmp = [numbers[index], numbers[start], numbers[end]]
                    result.append(tmp)
                    start+=1
                elif sum > 0:
                    end-=1
                elif sum < 0:
                    start+=1
        return result
