"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


# class PriorityQueue:
#     def __init__(self):
#         self.pr_q = []
#
#     def enqueue(self, elem: Any, priority: int = 0) -> None:
#         """
#         Operation that add element to the end of the queue
#
#         :param elem: element to be added
#         :return: Nothing
#         """
#
#         item = {
#             "elem": elem,
#             "priority": priority
#         }
#
#         if not self.pr_q:
#             self.pr_q.append(item)
#             return None
#
#         for index, current_item in enumerate(self.pr_q):
#             if current_item["priority"] <= item["priority"]:
#                 self.pr_q.insert(index, item)
#                 break
#         else:
#             self.pr_q.append(item)
#
#     def dequeue(self) -> Any:
#         """
#         Return element from the beginning of the queue. Should return None if not elements.
#
#         :return: dequeued element
#         """
#
#         if not self.pr_q:
#             return None
#
#         return self.pr_q.pop()["elem"]
#
#     def peek(self, ind: int = 0, priority: int = 0) -> Any:
#         """
#         Allow you to see at the element in the queue without dequeuing it
#
#         :param ind: index of element (count from the beginning)
#         :return: peeked element
#         """
#
#         return self.pr_q[-1 - ind]["elem"]
#
#     def clear(self) -> None:
#         """
#         Clear my queue
#
#         :return: None
#         """
#         self.pr_q.clear()
#
#         return None


class PriorityQueue:
    def __init__(self):
        self.pr_q = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
        }

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """

        mini_q = self.pr_q[priority]
        mini_q.append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """

        for i in range(len(self.pr_q)):
            if self.pr_q[i]:
                return self.pr_q[i].pop(0)

        return None

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """

        for i in range(len(self.pr_q)):
            if self.pr_q[i]:
                try:
                    return self.pr_q[i][ind]
                except IndexError:
                    ind = 0

        return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """

        self.pr_q = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
        }

        return