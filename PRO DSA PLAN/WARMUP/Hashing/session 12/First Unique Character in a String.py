# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:

        hashmap = {}

        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i],0)

        temp = -1
        for i in hashmap.keys():
            if hashmap[i] == 1:
                temp = i
                break
        for i in range(len(s)):
            if s[i] == temp:
                temp = i
        return temp 
        