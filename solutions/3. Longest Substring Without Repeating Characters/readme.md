## [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

>Given a string `s`, find the length of the **longest substring** without repeating characters.

Use one single pointer iterate through every char of the string, and with variable `start` recording the current substring without repeat char. Keep every char and its position in hash table for fast search (O(1)).

Whenever encountering a repeat char, all we need is to update the start of the target substring to be the next position of the repeat char (previous one). Anyway if this position is less than `start`, we won't update start (won't go back). 

That is to say, only the repeat char in the range of target substring is what we care about, which will be the pivot point for updating `start`. Those repeat chars in the position before current `start` are irrelevant. 

The length of current substring is `j - start + 1`. So in every iteration, just update max length to be the greater one of `maxlen, j - start + 1`.

- Time complexity: O(n)
- Space complexity: O(n)

```python
class Solution:
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
```


<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
