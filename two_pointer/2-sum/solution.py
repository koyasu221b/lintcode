class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        return self.solved_by_two_point(numbers, target)

    def solved_by_two_point(self, numbers, target):
        # write your code here
        tmp = []
        for index, number in enumerate(numbers):
            tmp.append((number,index))

        tmp = sorted(tmp)
        left = 0
        right = len(numbers) - 1
        while left < right:
            left_number = tmp[left][0]
            right_number = tmp[right][0]
            sum = left_number + right_number
            if sum > target:
                right-=1
            elif sum < target:
                left+=1
            else:
                return sorted([tmp[left][1]+1, tmp[right][1]+1])

        return []


    def solved_by_hash(self, numbers, target):
        hash  = {}
        for index, num in enumerate(numbers):
            hash[num] = index

        result = []
        for index, number in enumerate(numbers):
            if (target - number) in numbers:
                result = [index+1, hash[target-number]+1]
                return sorted(result)

        return []
