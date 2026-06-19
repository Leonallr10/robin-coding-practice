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
    
    def insertatbeg(self, data, head):
        new_node = Node(data)
        new_node.next = head
        return new_node
    
    def insertatend(self, data, head):
        new_node = Node(data)
        if head is None:
            return new_node
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return head
    
    
    def insertatpos(self, data, pos, head):
        new_node = Node(data)
        if pos ==0:
            new_node.next = head
            return new_node
        curr = head
        for i in range(pos-1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        return head

    
    def deletefr(self, head):
        if head is None:
            return None
        return head.next
        
    def deletelast(self, head):
        if head is None or head.next is None:
            return None
        curr = head
        while curr.next.next:
            curr = curr.next
        curr.next = None
        return head

    def deleteatpos(self, pos, head):
        if pos == 0:
            return self.deletefr(head)
        curr = head
        for i in range(pos-1):
            curr = curr.next
        curr.next = curr.next.next
        return head
        

    
ll = Node(10)
ll.next = Node(20)
ll.next.next = Node(30)
sol = Solution()
print(sol.traverse(ll))
print(sol.countll(ll))
print(sol.searchll(20))
