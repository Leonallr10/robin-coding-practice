from decimal import HAVE_THREADS
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
    def countll(self, head:Node)-> int:
        count = 0
        curr = head 
        while curr:
            count +=1
            curr = curr.next
        return count
    def searchll(self, head, ele:int):
        curr = head
        while curr:
            if curr.data == ele:
                return ele
            curr=curr.next
        return -1

    def getele(self,head,index):
        curr = head
        count = 0
        while curr:
            if count == index:
                return curr.data
            curr = curr.next
            count+=1
        return -1   
    
    def insertll(self, data, head):
        new_node = Node(data)
        new_node.next = head
        return new_node

    
ll = Node(10)
ll.next = Node(20)
ll.next.next = Node(30)
sol = Solution()
print(sol.traverse(ll))
print(sol.countll(ll))
print(sol.searchll(20))
