class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        temp = self.head
        while temp :
            print(str(temp.data) + "->", end = "")
            temp = temp.next

        print("Null")

    def reverseLinkedList(self):

        current = self.head
        prev = None
        while current != None :
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev



if __name__ == "__main__":

    nums = list(input("enter number array : ").split(" "))

    print(nums)
    llist = LinkedList()

    #llist.head = Node(1)
    #second  = Node(2)
    #third = Node(3)

    prev = llist.head

    for i in range(len(nums)):
        node = Node(nums[i])

        if i == 0 :
            llist.head = node
        else : 
            prev.next = node

        prev = node

    #llist.head.next = second
    #second.next = third

    llist.printList()

    llist.reverseLinkedList()
    llist.printList()