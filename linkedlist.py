class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def traverse(self,head:Node) -> str:
        ele = []
        curr = head
        while curr:
            ele.append(curr.data)
            curr = curr.next
        return ele
    def countll(self, head:Node)-> str:
        count = 0
        curr = head 
        while curr:
            count +=1
            curr = curr.next
        return count

ll = Node(10)
ll.next = Node(20)
ll.next.next = Node(30)
sol = Solution()
print(sol.traverse(ll))
print(sol.countll(ll))
