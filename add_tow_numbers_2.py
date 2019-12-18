# 1. 这题关键是要思考清楚程序的停止条件是 l1, l2, carrier 都为空.
# 2. 程序的主要工作是将两个节点和carrier相加后得到新的节点值.


def print_list(list):
    tmp = ""
    while list:
        tmp += " %u " % list.val
        list = list.next
    print(tmp)


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def append(self, node):
        self.next = node
        return node


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode(0)
    tmp = l3
    carrier = 0
    while True:

        if l1:
            carrier += l1.val

        if l2:
            carrier += l2.val

        carrier, left = carrier // 10, carrier % 10
        tmp.val = left

        if l1:
            l1 = l1.next

        if l2:
            l2 = l2.next

        if not l1 and not l2 and not carrier:
            break
            
        tmp.next = ListNode(0)
        tmp = tmp.next

    return l3


if __name__ == "__main__":
    l1 = ListNode(9)
    tmp = l1.append(ListNode(8))
    # print_list(l1)
    l2 = ListNode(1)
    # print_list(l2)
    ans = addTwoNumbers(l1, l2)
    print_list(ans)
