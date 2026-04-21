from __future__ import annotations

#sebuah linked list
class Node:
    def __init__(self, value, next=None):
        self.value:int = value
        self.next: Node | None = next
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        #this wills set the head of the linkedlist
        self.head: Node | None = None

    def append(self, value: int):
        #append a new node to the end of the linked list
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return 
        
        #if it is not the first node then we need to traverse the linked lis until it is node
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def traverse_liked_list(self, node: Node):
        #first we need to check if the current node is not noe
        if node is None:
            return 
        while node.next is not None:
            print(node.value)
            node = node.next
        
        #print the last value
        print(node.value)
        
    def access_node(self, node: Node, target: int):
        #access the node with the specific index
        index = 0
        while node:
            if node.value == target:
                return index
            node = node.next
            index +=1
        return -1

def main():
    #test dlu linked list nya
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.traverse_liked_list(l1.head)
    index =l1.access_node(l1.head, 2)
    print(index)

if __name__ == "__main__":
    main()