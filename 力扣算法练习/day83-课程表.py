# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 9:31
# @Author  : Xin
# @File    : day83-课程表.py
# @Software: PyCharm

# 现在你总共有 n 门课需要选，记为 0 到 n-1。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
#
# 给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
# 示例 2:
#
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
# 说明:
#
# 输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 提示:
#
# 这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
# 通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
# 拓扑排序也可以通过 BFS 完成。

'''
思路1：拓扑排序。构建的邻接表就是我们通常认识的邻接表，每一个结点存放的是后继结点的集合。
该方法的每一步总是输出当前无前趋（即入度为零）的顶点。为避免每次选入度为 $0$ 的顶点时扫描整个存储空间，可设置一个队列暂存所有入度为 $0$ 的顶点。
具体做法如下：
1、在开始排序前，扫描对应的存储空间，将入度为 0 的顶点均入队列。
2、只要队列非空，就从队首取出入度为 0 的顶点，将这个顶点输出到结果集中，并且将这个顶点的所有邻接点的入度减 1，在减 1 以后，发现这个邻接点的入度为 0 ，就继续入队。
最后检查结果集中的顶点个数是否和课程数相同即可。
'''
class Solution(object):
    # 思想：该方法的每一步总是输出当前无前趋（即入度为零）的顶点
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int 课程门数
        :type prerequisites: List[List[int]] 课程与课程之间的关系
        :rtype: bool
        """
        # 课程的长度
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return True
        # 入度数组，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表
        adj = [set() for _ in range(numCourses)]

        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # [0,1] 表示 1 在先，0 在后
        # 注意：邻接表存放的是后继 successor 结点的集合
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)

        print("in_degrees", in_degrees)
        # 首先遍历一遍，把所有入度为 0 的结点加入队列
        res = []
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        counter = 0
        while queue:
            top = queue.pop(0)
            counter += 1

            for successor in adj[top]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    queue.append(successor)

        return counter == numCourses


numCourses=2
prerequisites=[[0,1]]
s= Solution()
print(s.canFinish(numCourses,prerequisites))



'''
思路2：构建逆邻接表，实现深度优先遍历。思路其实也很简单，其实就是检测这个有向图中有没有环，只要存在环，课程就不能完成。
注意：这个深度优先遍历得通过逆邻接表实现，当访问一个结点的时候，应该递归访问它的前驱结点，直至前驱结点没有前驱结点为止。
'''

# class Solution(object):
#
#     # 这里使用逆邻接表
#
#     def canFinish(self, numCourses, prerequisites):
#         """
#         :type numCourses: int 课程门数
#         :type prerequisites: List[List[int]] 课程与课程之间的关系
#         :rtype: bool
#         """
#         # 课程的长度
#         clen = len(prerequisites)
#         if clen == 0:
#             # 没有课程，当然可以完成课程的学习
#             return True
#         # 深度优先遍历，判断结点是否访问过
#         # 这里要设置 3 个状态
#         # 0 就对应 False ，表示结点没有访问过
#         # 1 就对应 True ，表示结点已经访问过，在深度优先遍历结束以后才置为 1
#         # 2 表示当前正在遍历的结点，如果在深度优先遍历的过程中，
#         # 有遇到状态为 2 的结点，就表示这个图中存在环
#         visited = [0 for _ in range(numCourses)]
#
#         # 逆邻接表，存的是每个结点的前驱结点的集合
#         # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
#         # 1 在前，0 在后
#         inverse_adj = [set() for _ in range(numCourses)]
#         for second, first in prerequisites:
#             inverse_adj[second].add(first)
#
#         for i in range(numCourses):
#             # 在遍历的过程中，如果发现有环，就退出
#             if self.__dfs(i, inverse_adj, visited):
#                 return False
#         return True
#
#     def __dfs(self, vertex, inverse_adj, visited):
#         """
#         注意：这个递归方法的返回值是返回是否有环
#         :param vertex: 结点的索引
#         :param inverse_adj: 逆邻接表，记录的是当前结点的前驱结点的集合
#         :param visited: 记录了结点是否被访问过，2 表示当前正在 DFS 这个结点
#         :return: 是否有环
#         """
#         # 2 表示这个结点正在访问
#         if visited[vertex] == 2:
#             # 表示遇到环
#             return True
#         if visited[vertex] == 1:
#             return False
#
#         visited[vertex] = 2
#         for precursor in inverse_adj[vertex]:
#             # 如果有环，就返回 True 表示有环
#             if self.__dfs(precursor, inverse_adj, visited):
#                 return True
#
#         # 1 表示访问结束
#         visited[vertex] = 1
#         return False
#
# numCourses=2
# prerequisites=[[0,1]]
# s= Solution()
# print(s.canFinish(numCourses,prerequisites))

