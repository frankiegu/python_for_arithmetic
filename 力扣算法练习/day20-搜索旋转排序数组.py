# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 21:21
# @Author  : Xin
# @File    : day20-搜索旋转排序数组.py
# @Software: PyCharm

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1


#解法一：暴力法，直接循环整个列表，时间复杂度为O(n)
# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         #nums = [4, 5, 6, 7, 0, 1, 2]
#         if nums.__contains__(target):
#             flag=0
#             for i in nums:
#                 if i == target:
#                     return flag
#                 flag+=1
#         return -1
#
# nums = [4, 5, 6, 7, 0, 1, 2]
# s = Solution()
# print(s.search(nums,3))

#解法二：二分法，找出旋转点，时间复杂度为O（log n）
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1
        left, right = 0, len(nums) - 1

        while (nums[left] != target and nums[right] != target and left < right - 1):
            mid = (left + right) // 2
            if (nums[left] <= nums[mid] and (nums[left] > target or nums[mid] < target)):
                left = mid
            elif (nums[mid] <= target <= nums[right]):
                left = mid
            else:
                right = mid
        if target == nums[left]:
            return left
        elif target == nums[right]:
            return right
        else:
            return -1


nums = [4, 5, 6, 7, 0, 1, 2]
s = Solution()
print(s.search(nums,0))
