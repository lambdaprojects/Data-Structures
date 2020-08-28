"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # Creates a new node with value
        new_node = ListNode(value)

        # Increment the length of the doubly linked list by 1
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #Check if there is a head. Return none if no head
        node_value = self.head
        self.delete(self.head)
        return node_value.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # Create a new node with the value
        new_node = ListNode(value)

        #increment the value of the dll by 1
        self.length += 1

        #add the new node to the tail
        if not self.head and not self.tail:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        node_value = self.tail
        self.delete(self.tail)
        return node_value.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return 
        
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(node.value)

    # def test_move_head_to_end(self):
    #     self.move_to_end(self.head)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = self.head.next
            node.delete()
        elif self.tail is node:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()
        self.length -= 1 
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.length == 0:
            return 0
        else:
            max_val = self.head.value
            cur_node = self.head.next
            while (cur_node):
                if (cur_node.value > max_val):
                    max_val = cur_node.value
                cur_node = cur_node.next
            return max_val

        

    def __str__(self):
        return 'DLL:(head:'+ self.head.value+' tail:'+self.tail.value+' Length is '+ str(self.length)+')'

# new_dll = DoublyLinkedList()

# new_dll.add_to_head("5")
# print(new_dll)
# new_dll.add_to_head("10")
# print(new_dll)
# new_dll.add_to_head("15")
# # new_dll.test_move_head_to_end()
# print(new_dll)
# new_dll.add_to_head("20")
# print(new_dll)
# new_dll.add_to_head("25")
# print(new_dll)