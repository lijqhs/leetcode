class Solution:
    """
    dual pointers, sliding window, brute force version
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        maxlen = 0

        for i in range(len(s)):
            len_str_sliding = 0
            for j in range(i, len(s)):
                if ord(s[j]) not in sub:
                    sub.add(ord(s[j]))
                    len_str_sliding += 1
                else:
                    sub.clear()
                    break

            if maxlen < len_str_sliding:
                maxlen = len_str_sliding

        return maxlen


class Solution2:
    """
    dual pointers, skip i

    abcdefcghi, when j break, i restart from next position of first c
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        subchar = dict()
        maxlen = 0

        i = 0
        while i < len(s):
            len_str_sliding = 0
            for j in range(i, len(s)):
                if ord(s[j]) not in subchar.keys():
                    subchar[ord(s[j])] = j
                    len_str_sliding += 1
                else:
                    i = subchar[ord(s[j])] + 1
                    subchar.clear()
                    break

            if maxlen < len_str_sliding:
                maxlen = len_str_sliding

        return maxlen


class Solution3:
    """
    single pointer version of Solution2

    abcdefcghi
    record every pos in dictionary, when repeat, "remove" all char before (set value to -1), and
    deduct the length
    continue counting from the next position of repeat char 
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        subchar = dict()
        maxlen = 0

        len_str_sliding = 0

        for j in range(len(s)):
            if ord(s[j]) in subchar.keys() and subchar[ord(s[j])] >= 0:
                # when encounter repeat char, save the max length so far
                if maxlen < len_str_sliding:
                    maxlen = len_str_sliding

                # start over from next pos of repeat char by 
                # "removing" chars before, and
                # deducting the current substr length
                pos_repeat = subchar[ord(s[j])]     # pos of repeat char 
                for k,v in subchar.items():
                    if (v >= 0 and v <= pos_repeat):
                        # subchar.pop(k)
                        subchar[k] = -1
                        len_str_sliding -= 1
        
            subchar[ord(s[j])] = j
            len_str_sliding += 1

        if maxlen < len_str_sliding:
            maxlen = len_str_sliding

        return maxlen


class Solution4:
    """
    single pointer
    
    record every pos in dictionary
    when having repeat char, all we need is to update the start of substring
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_table = dict()
        maxlen = 0

        start = 0   # record the start pos of substring
        for j in range(len(s)):
            if ord(s[j]) in char_table.keys():
                start = max(start, char_table[ord(s[j])] + 1)  # update start pos if elligible
        
            maxlen = max(maxlen, j - start + 1) # update max length so far
            char_table[ord(s[j])] = j

        return maxlen


class Solution41:
    """
    single pointer
    
    record every pos in dictionary
    when having repeat char, all we need is to update the start of substring
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_table = dict()
        maxlen = 0
        start = 0   # record the start pos of substring
        for j, c in enumerate(s):
            if c in char_table:
                start = max(start, char_table[c] + 1)  # update start pos if elligible
        
            maxlen = max(maxlen, j - start + 1) # update max length so far
            char_table[c] = j

        return maxlen


if __name__ == '__main__':
    # s = " "
    # s = "abcabcbb"
    # s = 'dvdf'
    # s = 'pwwkew'
    s = "abcdefcghi"
    # s = "loddktdji"
    solution = Solution41()
    print("longest length: ", solution.lengthOfLongestSubstring(s))