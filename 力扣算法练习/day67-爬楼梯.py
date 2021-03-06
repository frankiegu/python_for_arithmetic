# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 20:29
# @Author  : Xin
# @File    : day67-爬楼梯.py
# @Software: PyCharm

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶


#解法一:
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a =1
        b =1
        for i in range(n):
            a,b = b,a+b
        return a

n=5
s = Solution()
print(s.climbStairs(n))

#解法二:
# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 1:
#             return 1
#         dp = [0 for i in range(n+1)]
#         dp[1] = 1
#         dp[2] = 2
#         for i in range(3, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n]
#
# n=5
# s = Solution()
# print(s.climbStairs(n))