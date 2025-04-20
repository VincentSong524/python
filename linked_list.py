class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val                     # 节点值
        self.next: ListNode | None = None       # 指向下一节点的引用    
    
class DoubleListNode:
    """双向链表节点类"""
    def __init__(self, val: int):
        self.val: int = val                         # 节点值
        self.next: DoubleListNode | None = None     # 指向后继节点的引用
        self.prev: DoubleListNode | None = None     # 指向前驱节点的饮用
        

# 初始化链表 1 -> 3 -> 2 -> 5 -> 4
# 初始化各个节点
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)
# 构建节点之间的引用
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

def insert(n0: ListNode, P: ListNode):
    """在链表的节点 n0 之后插入节点 P"""
    temp = n0.next
    P.next = temp
    n0.next = P
    
def remove(n0: ListNode):
    """删除链表的节点 n0 之后的首个节点"""
    if not n0.next: # 如果是尾节点后面就没有节点了
        return
    # n0 -> P -> n1
    P = n0.next
    n1 = P.next
    n0.next = n1
    
def access(head: ListNode, index: int) -> ListNode | None:
    """访问链表中索引为 index 的节点"""
    for _ in range(index):
        if not head:            # 如果头节点不存在，证明是一个空链表
            return None
        head = head.next        # 将节点后移
    return head

def find(head: ListNode, target: int) -> int:
    """在链表中查找值为 target 的首个节点"""
    index = 0
    while head:
        if head.val == target:  # 找到了就返回 index
            return index
        head = head.next        # 节点后移
        index += 1
    return -1                   # 没找到就返回 -1