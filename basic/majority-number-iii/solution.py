class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        counters = {}
        for num in nums:
            if num in counters:
                counters[num] += 1
            else:
                counters[num] = 1


            if len(counters) >=k:
                remove_list = []
                for num, counter in counters.iteritems():
                    counters[num] -=1
                    if counters[num] == 0:
                        remove_list.append(num)
                for remove_number in remove_list:
                    del counters[remove_number]

        for num in counters:
            counters[num] = 0

        for num in nums:
            if num in counters:
                counters[num]+=1

        majority_number = 0
        max_counter = 0
        for num, counter in counters.iteritems():
            if counter > max_counter:
                majority_number = num
                max_counter = counter

        return majority_number
