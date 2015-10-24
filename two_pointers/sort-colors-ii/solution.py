class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        next_start_index = 0
        for i in range(k):
            start_index = next_start_index
            next_start_index = self.sort_color_helper(start_index, i+1, colors)


    def sort_color_helper(self, start_index, sort_color, colors):
        left = start_index
        right = len(colors)-1
        while left <= right:
            while left<=right and colors[left] == sort_color:
                left+=1
            while left<=right and colors[right] != sort_color:
                right-=1

            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]

        return left
