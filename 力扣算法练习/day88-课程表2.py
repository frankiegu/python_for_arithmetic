# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 7:35
# @Author  : Xin
# @File    : day88-课程表2.py
# @Software: PyCharm


# 现在你总共有 n 门课需要选，记为 0 到 n-1。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
#
# 给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
#
# 可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: [0,1]
# 解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
# 示例 2:
#
# 输入: 4, [[1,0],[2,0],[3,1],[3,2]]
# 输出: [0,1,2,3] or [0,2,1,3]
# 解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
#      因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
# 说明:
#
# 输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 提示:
#
# 这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
# 通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
# 拓扑排序也可以通过 BFS 完成。


# 思路1：拓扑排序。构建的邻接表就是我们通常认识的邻接表，每一个结点存放的是后继结点的集合。
# 该方法的每一步总是输出当前无前趋（即入度为零）的顶点。为避免每次选入度为 0 的顶点时扫描整个存储空间，可设置一个队列暂存所有入度为 0 的顶点。
# 具体做法如下：
# 1、在开始排序前，扫描对应的存储空间，将入度为 0 的顶点均入队列。
# 2、只要队列非空，就从队首取出入度为 0 的顶点，将这个顶点输出到结果集中，并且将这个顶点的所有邻接点的入度减 1，在减 1 以后，发现这个邻接点的入度为 0 ，就继续入队。
# 最后检查结果集中的顶点个数是否和课程数相同即可。

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int 课程门数
        :type prerequisites: List[List[int]] 课程与课程之间的关系
        :rtype: bool
        """
        # 课程的长度
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return [i for i in range(numCourses)]
        # 入度数组，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表
        adj = [set() for _ in range(numCourses)]
        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # 1 -> 0，这里要注意：不要弄反了
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)

        # print("in_degrees", in_degrees)
        # 首先遍历一遍，把所有入度为 0 的结点加入队列
        res = []
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        while queue:
            top = queue.pop(0)
            res.append(top)

            for successor in adj[top]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    queue.append(successor)
        if len(res) != numCourses:
            return []
        return res


# 思路2：构建逆邻接表，实现深度优先遍历。思路其实也很简单，其实就是检测这个有向图中有没有环，只要存在环，课程就不能完成。
# 注意：这个深度优先遍历得通过逆邻接表实现，当访问一个结点的时候，应该递归访问它的前驱结点，直至前驱结点没有前驱结点为止。

# class Solution(object):
#     def findOrder(self, numCourses, prerequisites):
#         """
#         :type numCourses: int 课程门数
#         :type prerequisites: List[List[int]] 课程与课程之间的关系
#         :rtype: bool
#         """
#         # 课程的长度
#         clen = len(prerequisites)
#         if clen == 0:
#             # 没有课程，当然可以完成课程的学习
#             return [i for i in range(numCourses)]
#
#         # 逆邻接表
#         inverse_adj = [set() for _ in range(numCourses)]
#         # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
#         # 1 -> 0，这里要注意：不要弄反了
#         for second, first in prerequisites:
#             inverse_adj[second].add(first)
#
#         visited = [0 for _ in range(numCourses)]
#         # print("in_degrees", in_degrees)
#         # 首先遍历一遍，把所有入度为 0 的结点加入队列
#
#         res = []
#         for i in range(numCourses):
#             if self.__dfs(i,inverse_adj, visited, res):
#                 return []
#         return res
#
#     def __dfs(self, vertex, inverse_adj, visited, res):
#         """
#         注意：这个递归方法的返回值是返回是否有环
#         :param vertex: 结点的索引
#         :param inverse_adj: 逆邻接表，记录的是当前结点的前驱结点的集合
#         :param visited: 记录了结点是否被访问过，2 表示当前正在 DFS 这个结点
#         :return: 是否有环
#         """
#         # 2 表示这个结点正在访问
#         if visited[vertex] == 2:
#             # DFS 的时候如果遇到一样的结点，就表示图中有环，课程任务便不能完成
#             return True
#         if visited[vertex] == 1:
#             return False
#         # 表示正在访问这个结点
#         visited[vertex] = 2
#         # 递归访问前驱结点
#         for precursor in inverse_adj[vertex]:
#             # 如果没有环，就返回 False，
#             # 执行以后，逆拓扑序列就存在 res 中
#             if self.__dfs(precursor, inverse_adj, visited, res):
#                 return True
#
#         # 能走到这里，说明所有的前驱结点都访问完了，所以可以输出了
#         # 并且将这个结点状态置为 1
#         visited[vertex] = 1
#
#         # 先把 vertex 这个结点的所有前驱结点都输出之后，再输出自己
#         res.append(vertex)
#         # 最后不要忘记返回 False 表示无环
#         return False
