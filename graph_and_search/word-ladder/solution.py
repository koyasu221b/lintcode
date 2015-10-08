class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        from Queue import Queue
        queue = Queue()
        queue.put(start)
        length = 1
        visited = {}
        while not queue.empty():
            length += 1
            size = queue.qsize()
            for i in range(size):
                current_word = queue.get()
                next_words = self.get_next_words(current_word, dict)
                for next_word in next_words:
                    if visited.get(next_word) is not None:
                        continue

                    if next_word == end:
                        return length
                    visited[next_word] = True
                    queue.put(next_word)

        return 0

    def get_next_words(self, current_word, dict):
        next_words = []
        # 'a' => 'z'
        for c in range(97,123):
            for index in range(len(current_word)):
                if chr(c) == current_word[index]:
                    continue
                tmp = list(current_word)
                tmp[index] = chr(c)
                new_word = ''.join(tmp)
                if new_word in dict:
                    next_words.append(new_word)
        return next_words
