# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 21:29
# @Author  : Xin
# @File    : day74-单词拆分.py
# @Software: PyCharm

# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false

#解法一：
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         if not s :
#             return True
#         ans = [0]
#         for i in range(len(s)+1):
#             for j in ans:
#                 if s[j:i] in wordDict:
#                     ans.append(i)
#                     break
#         return ans[-1] == len(s)
#
# temp = "leetcode"
# wordDict = ["leet", "code"]
# s = Solution()
# print(s.wordBreak(temp,wordDict))

#解法二：
class Solution:
    def wordBreak(self, s, wordDict):
        result, max_len = [0], 0
        for each in wordDict:
            if len(each) > max_len:
                max_len = len(each)
        for i in range(1, len(s)+1):
            for j in result:
                if i-j <= max_len and s[j:i] in wordDict:
                    result.append(i)
                    break
        return result[-1] == len(s)

temp = "leetcode"
wordDict = ["leet", "code"]
s = Solution()
print(s.wordBreak(temp,wordDict))
