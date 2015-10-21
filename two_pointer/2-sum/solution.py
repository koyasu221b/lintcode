class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        hash  = {}
        for index, num in enumerate(numbers):
            hash[num] = index

        result = []
        for index, number in enumerate(numbers):
            if (target - number) in numbers:
                result = [index+1, hash[target-number]+1]
                return sorted(result)

        return []
