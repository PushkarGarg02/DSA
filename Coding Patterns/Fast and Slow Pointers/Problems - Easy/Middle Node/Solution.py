class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Solution:
    def findMiddleNode(self, head):
        slow, fast = head, head
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        
        return slow.value
    

def main():
    sol = Solution()
    head = Node(1)
    print("Middle node is: " + str(sol.findMiddleNode(head))) #expect 1

    head.next = Node(2)
    print("Middle node is: " + str(sol.findMiddleNode(head))) #expect 2

    head.next.next = Node(3)
    print("Middle node is: " + str(sol.findMiddleNode(head))) #expect 2

    head.next.next.next = Node(4)
    print("Middle node is: " + str(sol.findMiddleNode(head))) #expect 3

    head.next.next.next.next = Node(5)
    print("Middle node is: " + str(sol.findMiddleNode(head))) #expect 3
    
    head.next.next.next.next.next = Node(6)
    print("Middle node is: " + str(sol.findMiddleNode(head))) #expect 4

    head.next.next.next.next.next.next = Node(7)
    print("Middle node is: " + str(sol.findMiddleNode(head))) #expect 4

main()