# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 21:44
# @Author  : Xin
# @File    : day91-将有序数组转换为二叉搜索树.py
# @Software: PyCharm


# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        else:
            mid=len(nums)//2
            tn=TreeNode(nums[mid])
            nums1=nums[0:mid]
            nums2=nums[mid+1:len(nums)]
            tn.left=self.sortedArrayToBST(nums1)
            tn.right=self.sortedArrayToBST(nums2)
        return tn

